[app]

title = Kiwi Finalizer
package.name = kiwifinalizer
package.domain = org.example

source.dir = .
source.include_exts = py,kv,jpg,png

version = 1.0

requirements = python3,kivy,kivymd,pillow,reportlab,python-docx,pyjnius,plyer

orientation = portrait

android.permissions = INTERNET,READ_MEDIA_IMAGES

android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools_version = 34.0.0

fullscreen = 0

android.request_legacy_storage = True