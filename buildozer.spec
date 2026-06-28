[app]
title = AngerAI
package.name = angerai
package.domain = org.angerai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Указываем фиксированные, стабильные версии
android.sdk_build_tools_version = 33.0.0
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
