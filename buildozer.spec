# ------------------------------------------------------------------
#  buildozer.spec  –  Bell Alarm (Kivy + KivyMD + Telegram-Bot)
# ------------------------------------------------------------------

[app]
title             = Bell Alarm
package.name      = bellalarm
package.domain    = org.example          # <- gern anpassen (z. B. com.yourname)

# Hauptskript / Verzeichnis
source.dir        = .                    # Repo-Root enthält die .py-Dateien
entrypoint        = telegram_alarm_app_material.py

# Versionsverwaltung (nur **eine** der beiden Varianten setzen!)
version           = 1.0.0                # manuelle Vergabe
# version.regex   = __version__ = ['"](.*)['"]   # ← Alternative: aus Code auslesen

orientation       = portrait
fullscreen        = 0                    # 1 = echte Vollbild-App, 0 = Status-Bar bleibt

# ------------------------------------------------------------------
#  Python-Abhängigkeiten  (nur reine Py-Wheels – native Teile brauchen Rezepte)
# ------------------------------------------------------------------
# Wichtig: *kein* "python3" hier aufführen – das bringt p4a selbst mit.
requirements      = python3,kivy==2.2.1,kivymd,plyer,python-telegram-bot==20.7

# ------------------------------------------------------------------
#  Android-Spezifisches
# ------------------------------------------------------------------
# Neue Syntax mit „android.archs“
android.archs     = arm64-v8a,armeabi-v7a      # 64- & 32-Bit APKs

# Welche SDK-/NDK-Installation Buildozer nutzen soll
android.sdk_path  = /home/runner/android-sdk
android.ndk_path  = /home/runner/android-sdk/ndk/25.2.9519653

android.api       = 34          # Ziel-API (zu den installierten Build-Tools passen)
android.ndk_api   = 21          # Minimal-API, ab der NDK-Libs kompiliert werden
android.minapi    = 21          # minimal unterstützte Geräte-Version

# Akzeptiere Google-Lizenzen automatisch (CI/CD-geeignet)
android.accept_sdk_license = True

# Benötigte Berechtigungen
android.permissions = INTERNET, WAKE_LOCK

# ------------------------------------------------------------------
#  (Optionale) Ressourcen
# ------------------------------------------------------------------
# Icon   (512×512 PNG)   → ./data/icon.png
# Presplash-Bild         → ./data/presplash.png
icon.filename       = %(source.dir)s/data/icon.png
presplash.filename  = %(source.dir)s/data/presplash.png

# ------------------------------------------------------------------
#  Build- & Debug-Helfer
# ------------------------------------------------------------------
log_level           = 2              # 0 = quiet, 2 = verbose (gut für GitHub-Log)
# cmdline_log        = 1            # Setzen, falls ADB-Logs erwünscht
# android.logcat_filters = *:S python:I kivy:I

[buildozer]
# So findet Buildozer seine Tools auch lokal
warn_on_root = 1
