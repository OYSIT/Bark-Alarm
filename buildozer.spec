[app]
title = Bell Alarm
package.name = bellalarm
package.domain = org.example
source.dir = .
entrypoint = telegram_alarm_app_material.py
version = 1.0.0

# Archs – neue Syntax!
android.archs = arm64-v8a, armeabi-v7a

orientation = portrait
fullscreen = 0
# requirements ohne python3 (wird automatisch hinzugefügt)
requirements = kivy==2.2.1, kivymd, plyer, python-telegram-bot==20.7
