[app]
title = HelloApp
package.name = helloapp
package.domain = org.example.helloapp
source.dir = .
source.include_exts = py
version = 0.1
icon.filename = icon.png
orientation = portrait
android.permissions = INTERNET
buildozer.build_mode = release
requirements = kivy

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = ./build
bin_dir = ./bin
