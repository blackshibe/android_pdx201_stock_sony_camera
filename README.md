# Sony stock camera app patch (pdx201)

I recently found that the stock Sony cam app can be installed on custom ROMs just fine. This repo compiles all the required files to get it working.

## My testing

Tested on LineagOS 19.1, self-compiled from https://github.com/lineageos-on-pdx201

## Requirements

-   You need to be able to mount the system partition in recovery (or as read-write while the phone is on) and connect through adb shell.
-   You need a custom ROM which has all the required Sony cam libraries in the vendor partition.

## Guide

0. Reboot to recovery

1. Mount system in /system_mnt

```
adb shell mkdir /system_mnt
adb shell mount /dev/block/mapper/system_b /system_mnt # find the A/B slot you're using manually, and mount its' partition to /system_mnt. Mine is system_b
```

2. Import priv-app permissions to stop bootloop

```
adb push packages/etc/permissions/privapp-permissions-sony.xml /system_mnt/system/etc/permissions/privapp-permissions-sony.xml
```

3. Import camera app

```
adb push packages/priv-app/ArtFilterCamera-xxhdpi-release /system_mnt/system/priv-app/ArtFilterCamera-xxhdpi-release
adb push packages/priv-app/com.sonymobile.addoncamera.portraitselfie /system_mnt/system/priv-app/com.sonymobile.addoncamera.portraitselfie
adb push packages/priv-app/SemcCameraUI-xxhdpi-release /system_mnt/system/priv-app/SemcCameraUI-xxhdpi-release
adb push packages/priv-app/CameraPanorama-release /system_mnt/system/priv-app/CameraPanorama-release
```

4. Reboot to system

5. Make sure permissions are correct
    - Go to settings, find the Sony camera app, allow all permissions, start the app
