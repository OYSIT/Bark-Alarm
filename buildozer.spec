[app]
title          = Bark Alarm
package.name   = barkalarm
package.domain = org.example
version = 0.1.0
requirements = kivy==2.2.1,kivymd==1.2.0,plyer,pyjnius==1.6.1,python-telegram-bot==20.7,cython==0.29.36,setuptools,six
android.permissions = VIBRATE,WAKE_LOCK,INTERNET
android.api    = 34
android.ndk_api= 21
orientation    = portrait
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,ttc,wav,ogg,mp3,txt,json,xml
