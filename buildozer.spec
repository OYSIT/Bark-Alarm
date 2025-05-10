[app]
title = Bark Alarm
package.name = barkalarm
package.domain = org.example
version = 0.1

# Quellen
source.dir = .
source.include_exts = py,kv,png,jpg,json,ogg,wav,mp3

# Abhängigkeiten
requirements = python3,\
kivy==2.2.1,\
kivymd,\
plyer,\
python-telegram-bot==20.7,\
cython==0.29.36,\
pyjnius==1.6.1

# Android Plattform
android.api = 34
android.build_tools_version = 34.0.0
android.ndk = 25b
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.accept_sdk_license = True

# p4a-Extra: grp/pwd deaktivieren
android.p4a_args = --disable-python-stdlib-modules=grp,pwd

android.permissions = INTERNET,VIBRATE
log_level = 2
