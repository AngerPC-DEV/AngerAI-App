[app]
title = AngerAI
package.name = angerai
package.domain = org.angerai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
# Если используешь веб-вью, лучше проверь актуальность названия библиотеки
orientation = portrait
fullscreen = 0

# Настройки Android (теперь в блоке [app])
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
