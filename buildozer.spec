# buildozer.spec  – sauber & kompakt
[app]
title = Bark Alarm
package.name = barkalarm
package.domain = org.example
source.dir = .

# 1️⃣  Alles in **einer** Zeile, **ohne** Backslashes/Umbrüche
requirements = python3,kivy==2.2.1,kivymd==1.2.0,plyer,pyjnius==1.6.1,python-telegram-bot==20.7,cython==0.29.36,setuptools,six

android.permissions = VIBRATE,WAKE_LOCK,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET
android.ndk_api = 21
android.api = 34
orientation = portrait
presplash = %(source.dir)s/data/splash.png
