[app]

# معلومات التطبيق
title = Freebasics DDOS
package.name = ddos
package.domain = com.alrufaaey

# مسار المصادر
source.dir = ./src
source.include_exts = py,png,jpg,kv,txt,ttf,json

# إصدار التطبيق (يتم تحديثه تلقائياً من Git tags)
version.regex = __version__ = ['"]([^'"]*)['"]
version.filename = %(source.dir)s/main.py

# المتطلبات
requirements = 
    python3==3.9.15,
    kivy==2.1.0,
    https://github.com/kivymd/KivyMD/archive/master.zip,
    pyjnius==1.4.2,
    openssl,
    requests==2.28.2,
    pillow==9.5.0

# واجهة المستخدم
presplash.filename = ./assets/presplash.png
icon.filename = ./assets/ico.png
orientation = portrait
fullscreen = 0
log_level = 2

# إعدادات Android
[android]

# أذونات النظام
android.permissions = 
    INTERNET,
    ACCESS_NETWORK_STATE,
    ACCESS_WIFI_STATE,
    FOREGROUND_SERVICE,
    POST_NOTIFICATIONS,
    VIBRATE,
    WAKE_LOCK

# إصدارات API
android.api = 31
android.minapi = 21
android.sdk = 24
android.ndk = 25.2.9519653
android.ndk_api = 21

# هندسة المعالج (يتم تعيينه في CI)
android.arch = arm64-v8a

# إعدادات التطبيق
android.private_storage = True
android.wakelock = True
android.allow_backup = True
android.accept_sdk_license = True

# تكوين التوقيع (debug)
android.release_artifact = .apk
android.ant_verbose = False
android.ant_target = debug

# تحسينات الأداء
android.add_src = %(source.dir)s
android.add_resources = %(source.dir)s

# مسارات SDK (يتم تعيينها في CI)
android.sdk = $ANDROID_HOME
android.ndk_path = $ANDROID_NDK_HOME

[buildozer]

# إعدادات Buildozer
log_level = 2
warn_on_root = 1

# التخزين المؤقت للاعتمادات
buildozer.sources_dir = .buildozer/sources
buildozer.bin_dir = .buildozer/bin
buildozer.global_buildozer_dir = .buildozer

# إعدادات Cython
cythonize = 1
cython.verbose = 0
