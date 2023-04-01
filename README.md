1- Install the Java Development Kit (JDK) if you don't already have it installed:
```commandline
sudo apt-get update
sudo apt-get install default-jdk
```

2- Install the Android SDK Command Line Tools:
```commandline
sudo apt-get install android-sdk
```

3- Set the ANDROID_HOME environment variable to the path of the SDK directory:
```commandline
export ANDROID_HOME=/usr/lib/android-sdk
```

4- Install the Android SDK components you need using the sdkmanager command. For example, to install the latest Android platform and build tools, run:
```commandline
./sdkmanager "platforms;android-31" "build-tools;31.0.0"
```
If there was an error saying:
```text
Error: Could not determine SDK root.
Error: Either specify it explicitly with --sdk_root= or move this package into its expected location: <sdk>/cmdline-tools/latest/
```
Use this command instead:
```commandline
./sdkmanager --sdk_root=/usr/lib/android-sdk  "platforms;android-31" "build-tools;31.0.0"
```
5- Install the Android NDK:
- Go to the official Android NDK download page: https://developer.android.com/ndk/downloads.
- Choose the version of NDK you want to download, and click on the corresponding link.
- Once the download is complete, extract the downloaded archive to a directory of your choice. For example, you can extract it to /opt/android-ndk directory:
```commandline
sudo mkdir -p /opt/android-ndk
sudo tar xzf android-ndk-<version>-linux-x86_64.zip -C /opt/android-ndk
```
Make sure to replace <version> with the actual version number of the NDK you downloaded.
- Add the NDK directory to your system's PATH environment variable by adding the following line to your .bashrc or .bash_profile file:
```commandline
export PATH=$PATH:/opt/android-ndk/android-ndk-<version>
```
Again, make sure to replace <version> with the actual version number of the NDK you downloaded.
- Save the changes to your .bashrc or .bash_profile file, and source it to apply the changes:
```bash
source ~/.bashrc
```
- Verify that the NDK is installed and configured properly by running the following command:
```bash
ndk-build --version
```
This should display the version number of the NDK you installed.

OK, Now `android-sdk` and `android-ndk` are installed on the machine. Now we should install `buildozer`, a tool for building and packaging Kivy apps for Android:
- Install the required dependencies:
```commandline
sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3-setuptools \
    python3-venv \
    zlib1g-dev \
    openjdk-8-jdk \
    ant \
    libffi-dev \
    libssl-dev
```
- Now install buildozer:
```commandline
pip3 install --upgrade buildozer
```
- Test the installation:
```commandline
buildozer --version
```
This should display the version number of Buildozer that you just installed.
>Note that Buildozer requires Python 3.6 or later, so make sure that you have a compatible version of Python installed on your system. Also, the OpenJDK 8 package is required for Buildozer to work properly.
This is a `buildozer.spec` sample:
```text
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
```