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
sdkmanager "platforms;android-31" "build-tools;31.0.0"
```

5- Install the Android NDK:
```commandline
sudo apt-get install android-ndk
```
