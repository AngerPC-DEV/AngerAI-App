[app]
title = AngerAI
package.name = angerai
package.domain = org.angerai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivy-webview
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
