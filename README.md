# Python Sysadmin Tools

Eine Sammlung von Python-Skripten zur Automatisierung von Systemadministrationsaufgaben unter Linux (Ubuntu).

## Skripte

### 1. `disk_checker.py`
Ein einfaches Skript zur Überwachung des Speicherplatzes auf der Festplatte (`/`).
- Verwendet das eingebaute Python-Modul `shutil`.
- Gibt den gesamten, belegten und freien Speicherplatz in GB aus.
- Warnt automatisch, wenn die Belegung 90% überschreitet.

## Ausführung
```bash
python3 disk_checker.py