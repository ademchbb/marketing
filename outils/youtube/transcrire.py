#!/usr/bin/env python3
"""Récupère métadonnées + transcription d'une vidéo YouTube.

Usage : python3 outils/youtube/transcrire.py <url-ou-id> [<url-ou-id> ...]
Écrit dans sources/youtube/<id>/ :
  - metadata.json      (titre, chaîne, durée, date, vues, description, chapitres, tags)
  - transcription.md   (texte horodaté par blocs de ~30 s, lisible par un agent)
Stratégie : yt-dlp (sous-titres manuels > auto « -orig » > auto), puis
youtube-transcript-api en secours, avec plusieurs tentatives (YouTube renvoie
parfois 429 / RequestBlocked depuis les IP cloud).
"""
import json, re, subprocess, sys, tempfile, time
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
SORTIE = RACINE / "sources" / "youtube"
TENTATIVES = 5


def video_id(arg: str) -> str:
    m = re.search(r"(?:v=|youtu\.be/|shorts/|embed/)([A-Za-z0-9_-]{11})", arg)
    return m.group(1) if m else arg.strip()


def ts(sec: float) -> str:
    sec = int(sec)
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}" if sec >= 3600 else f"{sec // 60:02d}:{sec % 60:02d}"


def parse_vtt(texte: str):
    """VTT auto YouTube -> liste (debut_s, texte) sans doublons de défilement."""
    segs, vus = [], set()
    for bloc in texte.split("\n\n"):
        lignes = bloc.strip().splitlines()
        tl = next((l for l in lignes if "-->" in l), None)
        if not tl:
            continue
        h, m, s = tl.split("-->")[0].strip().split(":")
        debut = int(h) * 3600 + int(m) * 60 + float(s)
        for l in lignes[lignes.index(tl) + 1:]:
            l = re.sub(r"<[^>]+>", "", l).strip()
            if l and l not in vus:
                vus.add(l)
                segs.append((debut, l))
    return segs


def via_ytdlp(vid: str, tmp: Path):
    url = f"https://www.youtube.com/watch?v={vid}"
    meta = json.loads(subprocess.run(["yt-dlp", "-J", "--skip-download", url],
                                     capture_output=True, text=True, check=True, timeout=180).stdout)
    langue = meta.get("language") or "en"
    court = langue.split("-")[0]  # « fr-FR » -> « fr » : sinon on retombe sur une traduction anglaise
    manuels = meta.get("subtitles") or {}
    autos = meta.get("automatic_captions") or {}
    choix = None
    for l in [langue, court, "en", "fr"]:
        if l in manuels:
            choix = ("--write-subs", l); break
    if not choix:
        for l in [f"{langue}-orig", f"{court}-orig", langue, court, "en-orig", "en", "fr-orig", "fr"]:
            if l in autos:
                choix = ("--write-auto-subs", l); break
    segs = []
    if choix:
        subprocess.run(["yt-dlp", "--skip-download", choix[0], "--sub-langs", choix[1], "--sub-format", "vtt",
                        "-o", str(tmp / "%(id)s.%(ext)s"), url], capture_output=True, text=True, timeout=180)
        fichiers = list(tmp.glob(f"{vid}*.vtt"))
        if fichiers:
            segs = parse_vtt(fichiers[0].read_text(encoding="utf-8"))
    return meta, segs, (choix[1] if choix else None)


def via_api(vid: str):
    from youtube_transcript_api import YouTubeTranscriptApi
    tr = YouTubeTranscriptApi().fetch(vid, languages=["en", "fr", "es"])
    return [(s.start, s.text) for s in tr]


def ecrire(vid, meta, segs, langue):
    d = SORTIE / vid
    d.mkdir(parents=True, exist_ok=True)
    garder = ["id", "title", "channel", "uploader_id", "channel_follower_count", "duration", "upload_date",
              "view_count", "like_count", "comment_count", "description", "chapters", "tags", "categories", "language"]
    m = {k: meta.get(k) for k in garder} if meta else {"id": vid}
    m["url"] = f"https://www.youtube.com/watch?v={vid}"
    m["langue_transcription"] = langue
    m["nb_segments"] = len(segs)
    (d / "metadata.json").write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")
    lignes = [f"# {m.get('title') or vid}", "",
              f"- Chaîne : {m.get('channel')} · Durée : {ts(m.get('duration') or 0)} · Publiée : {m.get('upload_date')} · Vues : {m.get('view_count')}",
              f"- URL : {m['url']}", f"- Transcription : {langue} (automatique si suffixe -orig)", ""]
    chap = m.get("chapters") or []
    if chap:
        lignes += ["## Chapitres", ""] + [f"- [{ts(c['start_time'])}] {c['title']}" for c in chap] + [""]
    lignes += ["## Transcription", ""]
    bloc, debut = [], None
    for t, txt in segs:
        if debut is None:
            debut = t
        bloc.append(txt)
        if t - debut >= 30:
            lignes.append(f"**[{ts(debut)}]** " + " ".join(bloc)); lignes.append("")
            bloc, debut = [], None
    if bloc:
        lignes.append(f"**[{ts(debut)}]** " + " ".join(bloc))
    (d / "transcription.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return d


def traiter(arg):
    vid = video_id(arg)
    meta, segs, langue, erreur = None, [], None, None
    for i in range(TENTATIVES):
        try:
            with tempfile.TemporaryDirectory() as tmp:
                meta, segs, langue = via_ytdlp(vid, Path(tmp))
            if segs:
                break
        except Exception as e:  # noqa: BLE001
            erreur = e
        try:
            segs, langue = via_api(vid), "api"
            if segs:
                break
        except Exception as e:  # noqa: BLE001
            erreur = e
        time.sleep(2 ** (i + 1))
    if not segs:
        print(f"ÉCHEC {vid} : {type(erreur).__name__ if erreur else 'pas de sous-titres'}", file=sys.stderr)
        if meta:
            ecrire(vid, meta, [], None)
        return False
    d = ecrire(vid, meta, segs, langue)
    print(f"OK {vid} -> {d.relative_to(RACINE)} ({len(segs)} segments, {langue})")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ok = [traiter(a) for a in sys.argv[1:]]
    sys.exit(0 if all(ok) else 1)
