# Reden statt richten – Chat-AI-Personas

Persona-Dateien für Chat AI (GWDG) zum Workshop „Reden statt richten“ bei den Demokratietagen der Universität Kassel, 25.11.2026.

Eine Persona öffnet sich über `https://chat-ai.academiccloud.de/chat?import=<URL der JSON-Datei>`.

- `modelltest/`: dieselbe Debunker-Persona (Fallkarte 1) auf vier Modellen, um das Modell für den Workshop auszuwählen.
- `personas/`: die elf Workshop-Personas (sechs Debunker für Phase A, fünf Rollen für Phase B), Modell DeepSeek V4 Flash 0731.
- `personas_qr/`: QR-Codes zu den Import-Links, `links.txt`: alle Links.
- `vorbereiten.py`: setzt Modell und erzeugt Links und QR-Codes neu, z. B. `python3 vorbereiten.py --ordner personas --modell-id <ID> --modell-name "<Name>" --basis-url https://raw.githubusercontent.com/jzpsych/reden-statt-richten/main/personas/`
