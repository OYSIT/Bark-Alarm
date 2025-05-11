# -----------------------------------------------------------
#  buildozer.spec  –  Bell Alarm  (Kivy + KivyMD + Telegram)
# -----------------------------------------------------------

[app]
title           = Bell Alarm
package.name    = bellalarm
package.domain  = org.example
# gern anpassen

# Code-Pfad & Start-Datei
source.dir      = .
entrypoint      = telegram_alarm_app_material.py

# Versionsinfo  (genau **eine** Variante verwenden)
version         = 1.0.0

orientation     = portrait
fullscreen      = 0

# -----------------------------------------------------------
#  Python-Abhängigkeiten
# -----------------------------------------------------------
#requirements = cython==0.29.36,hostpython3,python3==3.11.12,kivy @ git+https://github.com/kivy/kivy.git@2.2.1,kivymd,plyer,pyjnius==1.5.0,python-telegram-bot==20.7
#requirements = cython==0.29.36,hostpython3,python3==3.11.12,kivy==2.2.1,kivymd,plyer,pyjnius==1.5.0,python-telegram-bot==20.7
#requirements = cython==0.29.36,python3==3.11.12,hostpython3,kivy @ git+https://github.com/kivy/kivy.git@2.2.1,kivymd,plyer,pyjnius==1.5.0,python-telegram-bot==20.7
requirements = hostpython3,cython==0.29.36,python3==3.11.12,kivy @ git+https://github.com/kivy/kivy.git@2.2.1,kivymd,plyer,pyjnius==1.5.0,python-telegram-bot==20.7

# -----------------------------------------------------------
#  Android-Einstellungen
# -----------------------------------------------------------
android.archs         = arm64-v8a,armeabi-v7a

# SDK/NDK – Pfade passen zu deinem GitHub-Action-Script
android.sdk_path      = /home/runner/android-sdk
android.ndk_path      = /home/runner/android-sdk/ndk/25.2.9519653

# **Keine Kommentare hinter die Zahlen setzen!**
android.api           = 34
android.ndk_api       = 21
android.minapi        = 21

android.accept_sdk_license = True
android.permissions   = INTERNET, WAKE_LOCK
android.add_python_ignore = Lib/test/.*,Lib/lib2to3/tests/.*

# -----------------------------------------------------------
#  Ressourcen (optional)
# -----------------------------------------------------------
icon.filename         = %(source.dir)s/data/icon.png
presplash.filename    = %(source.dir)s/data/presplash.png

# -----------------------------------------------------------
#  Logging
# -----------------------------------------------------------
log_level             = 2

[buildozer]
warn_on_root = 1

[p4a]
p4a.branch = develop
