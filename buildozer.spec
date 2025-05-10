
[app]
title = Bell Alarm
package.name = bellalarm
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,kv,json
version = 0.1
requirements = python3,kivy==2.2.1,kivymd,plyer,python-telegram-bot==20.7
orientation = portrait
android.permissions = INTERNET,VIBRATE
# ===== Android API & Lizenzen =====
android.api = 34               # <- zwingt Buildozer auf stabile API 34
android.accept_sdk_license = True

[buildozer]
log_level = 2
