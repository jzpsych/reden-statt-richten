#!/usr/bin/env python3
"""Setzt Modellname und Modell-ID in allen Persona-Dateien und erzeugt die Import-Links.

    python3 vorbereiten.py --modell-id qwen3.5-397b-a17b \
        --modell-name "Qwen 3.5 397B A17B" \
        --basis-url https://www.uni-kassel.de/.../personas/
"""
import argparse, json, pathlib, sys

CHAT = "https://chat-ai.academiccloud.de/chat?import="

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modell-id", required=True)
    ap.add_argument("--modell-name", required=True)
    ap.add_argument("--basis-url", help="öffentliche URL des Ordners, mit abschließendem /")
    ap.add_argument("--ordner", default=".")
    a = ap.parse_args()

    d = pathlib.Path(a.ordner)
    files = sorted(p for p in d.glob("*.json"))
    if not files:
        sys.exit(f"Keine JSON-Dateien in {d}/ gefunden.")

    for f in files:
        obj = json.loads(f.read_text(encoding="utf-8"))
        obj["model"] = a.modell_id
        obj["model-name"] = a.modell_name
        f.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(files)} Dateien auf Modell '{a.modell_id}' gesetzt.")

    if not a.basis_url:
        print("Ohne --basis-url werden keine Links erzeugt.")
        return

    base = a.basis_url if a.basis_url.endswith("/") else a.basis_url + "/"
    lines = [f"{f.name}\t{CHAT}{base}{f.name}" for f in files]
    pathlib.Path("links.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("links.txt geschrieben.")
    for ln in lines:
        print("  " + ln.replace("\t", "  ->  "))

    try:
        import qrcode
    except ImportError:
        print("\nModul 'qrcode' fehlt - QR-Codes nicht erzeugt (pip install \"qrcode[pil]\").")
        return
    out = pathlib.Path("qr"); out.mkdir(exist_ok=True)
    for f in files:
        qrcode.make(f"{CHAT}{base}{f.name}").save(out / f"{f.stem}.png")
    print(f"QR-Codes in {out}/ erzeugt.")

if __name__ == "__main__":
    main()
