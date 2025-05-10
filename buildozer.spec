############################################################################
# Basic information
############################################################################
[app]
title = Bell Alarm
package.name = bellalarm
package.domain = org.example        # ggf. ändern (z.B. com.yourname)
source.dir = .                      # Haupt-Python-Datei liegt im Repo-Root
entrypoint = telegram_alarm_app_material.py
version = 1.0.0
orientation = portrait
fullscreen = 0                      # 1 = Vollbild, 0 = Statusbar behalten

############################################################################
# Python / Kivy
############################################################################
# **KEIN** »python3« in der Liste – Buildozer fügt die Runtime selbst ein!
requirements = \
    kivy==2.2.1, \
    kivymd, \
    plyer, \
    python-telegram-bot==20.7

# Aktuelle Python-Runtime (auto)              -> 3.11-Recipe von p4a
# Cython + PyJNIus bringt Buildozer selbst mit

############################################################################
# Android build settings
############################################################################
android.api              = 34
android.minapi           = 21
android.ndk_api          = 21
# <<< NEU >>>
android.archs    = armeabi-v7a, arm64-v8a
# 32- und 64-bit
# → WICHTIG für CI/Runner ←
# Pfade auf den bereits installierten SDK/NDK verweisen,
# sonst lädt Buildozer alles doppelt und »aidl« fehlt.
android.sdk_path         = /home/runner/android-sdk
android.ndk_path         = /home/runner/android-sdk/ndk/25.2.9519653
android.accept_sdk_license = true

# Permissions (nur das, was wirklich gebraucht wird)
android.permissions = \
    INTERNET, \
    VIBRATE, \
    READ_EXTERNAL_STORAGE, \
    WRITE_EXTERNAL_STORAGE, \
    WAKE_LOCK

# Log-Level (1=normal, 2=sehr ausführlich)
log_level = 1

############################################################################
# Optional: Icons & VersionCode (Play Store)
############################################################################
# icon.filename = data/icon.png
# android.manifest_placeholders = appAuthRedirectScheme=custscheme
# android.numeric_version = 100        # 1.0.0 → 100
############################################################################
