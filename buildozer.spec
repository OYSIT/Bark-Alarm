####################################
# buildozer.spec – Bark Alarm
####################################

[app]
title = Bark Alarm
package.name = barkalarm
package.domain = org.example
version = 0.1
orientation = portrait

source.dir = .
source.include_exts = py,kv,png,jpg,json,ogg,wav,mp3

# Wichtig: Cython gepinnt, pyjnius explizit
requirements = \
    python3,\
    kivy==2.2.1,\
    kivymd,\
    plyer,\
    python-telegram-bot==20.7,\
    cython==0.29.36,\
    pyjnius==1.6.1

android.api = 34
android.build_tools_version = 34.0.0
android.ndk = 25b
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.accept_sdk_license = True

android.permissions = INTERNET,VIBRATE

copy_libs = 1
log_level = 2   # ausführliches Log

####################################
# Ende [app]
####################################

[buildozer]
# Standard bleibt unverändert
