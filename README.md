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
```commandline
source ~/.bashrc
```
- Verify that the NDK is installed and configured properly by running the following command:
```commandline
ndk-build --version
```
This should display the version number of the NDK you installed.