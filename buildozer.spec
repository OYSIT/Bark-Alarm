
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
android.api = 34
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

# ⇣  feste Pfade OHNE $HOME – auf GitHub heißt HOME immer /home/runner
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.accept_sdk_license = True
[buildozer]
log_level = 2
