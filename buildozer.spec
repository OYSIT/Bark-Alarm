####################################
# buildozer.spec – Bark Alarm
####################################

[app]

# -- Basisangaben --
title = Bark Alarm
package.name = barkalarm
package.domain = org.example
version = 0.1
orientation = portrait

# -- Quellordner & Dateitypen --
source.dir = .
source.include_exts = py,kv,png,jpg,json,ogg,wav,mp3

# -- Python & Abhängigkeiten --
# Achtung: Cython + pyjnius sind nötig, damit jnius.c gebaut wird
requirements = \
    python3,\
    kivy==2.2.1,\
    kivymd,\
    plyer,\
    python-telegram-bot==20.7,\
    cython,\
    pyjnius==1.6.1    # zu Kivy 2.2/NDK 25b kompatibel

# -- Android-SDK/NDK (passen exakt zu deinem Workflow) --
android.api = 34
android.ndk = 25b
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.sdk_path = /home/runner/android-sdk
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

# -- Berechtigungen --
android.permissions = INTERNET,VIBRATE

# -- Sonstiges --
copy_libs = 1                # Bibliotheken ins APK kopieren
log_level = 2                # ausführliches Buildozer-Log

####################################
# Ende [app]-Block
####################################


[buildozer]
# Standardwerte – hier nichts ändern, außer du brauchst spezielle Flags
############
