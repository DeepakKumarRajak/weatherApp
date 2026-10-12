[app]

# (str) Title of your application
title = Weather App

# (str) Package name
package.name = weatherapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty for all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of exclusions using pattern matching
source.exclude_patterns = */.git/*, */__pycache__/*, *.pyc, *.pyo

# (str) Application versioning (numeric) - should be 1 or greater
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android SDK directory (if empty, it will be auto-detected)
# android.sdk_path =

# (str) Android NDK directory (if empty, it will be auto-detected)
# android.ndk_path =

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Android archs to build for
android.archs = arm64-v8a

# (bool) If True, then default to -Xms1024m -Xmx4096m for Java builds
# android.javac.options = -Xms1024m -Xmx4096m

# (bool) If True, use the same package name for all versions
# android.allow_backup = True

# (str) The Android logcat filters to use
# android.logcat_filters = *:S python:D

# (str) The Android packaging tool
author = Your Name

# (str) When in debug mode, this option bumps the version number of the APK
# --

[buildozer]
# (int) Log level (0 = quiet, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning level (0 = quiet, 1 = info, 2 = debug)
warn_on_root = 0

# (str) Path to buildozer directory
# build_dir = .buildozer

# (str) Path to buildozer output directory
# bin_dir = ./bin

# -----------------------------------------------------------------------------
#       END OF FILE
# -----------------------------------------------------------------------------
