# Build VirtualBox in Windows

## Introduction

[This repository](https://github.com/VirtualBoBs/build-virtualbox-in-windows) provides a set of scripts which will help you compile VirtualBox easily.

You can find the official manual to compile VirtualBox in Windows from [the official site](https://www.virtualbox.org/wiki/Windows%20build%20instructions), but it's too obsolete to follow at this time. So, we wrote python scripts which prepare required libraries for compilation, and compile VirtualBox automatically.

What you need to do is only to install pre-requisites for the compilation, and run the scripts.

## Features

- It downloads or compiles the followings: 7-Zip, MinGW, SDL, SSL, cURL, Qt5
- It creates and registers a credential which is needed to compile drivers in Windows.
- It manages dependencies in the compilation.
- It compiles VirtualBox binaries.

## Requirement

- Windows 10
- Python (≥ 3.8)
- Enough spaces (at least 20GB)

## Building

To build VirtualBox via the scripts, you should follow the steps below.

### 1. Set Up Environment

Before using the scripts, you need to install the followings.

- Visual Studio 2010 (≥ **Professional**)
- [Visual Studio 2010 SP1](https://kovepg.tistory.com/entry/비주얼-스튜디오-2010-서비스팩1Visual-Studio-2010-SP1-설치파일)
- [WinSDK 7.1](https://www.microsoft.com/en-us/download/details.aspx?id=8279)
- [WinSDK 8.1](https://developer.microsoft.com/ko-kr/windows/downloads/sdk-archive/)
- [WinDDK 7.1](https://www.microsoft.com/en-us/download/details.aspx?displaylang=en&id=11800)
- [SSL 32bit](https://slproweb.com/download/Win32OpenSSL-1_1_1i.exe)
- [SSL 64bit](https://slproweb.com/download/Win64OpenSSL-1_1_1i.exe)

If at least one of them is not installed properly, you could be in trouble with compile errors afterwards. And, we recommend you install them **in their default paths**.

### 2. Set Up Privilege

Before going into any steps, you should satisfy the followings:

- Test Mode
- Root Privilege

You can turn on the test mode with the following:

```cmd
bcdedit /set testsigning on
```

Note that **you MUST reboot your PC** when you turned on the test mode **for the first time**.

And, you should execute any scripts in this repository **with root-privilege(Administrator)**. Unless, you will confront unexpected issues afterwards.

### 3. Download Source of VirtualBox

You should download from [the official site](https://www.virtualbox.org/wiki/Downloads) the sources of VirtualBox, which you want to compile. And copy the sources into `C:/VBoxBuild/VirtualBox`. Scripts will use `C:/VBoxBuild` as a default working directory for compilation.

### 4, Clone This Repository

Clone this repository via:

```cmd
git clone https://github.com/VirtualBoBs/build-virtualbox-in-windows.git
```

### 5. Run Setup Script

Run `script/setup.py`.

It will configure all the requirements for your compilation.

### 6. Run Build Script

Run `script/build.py`.

Please make sure that **the prior setup stage has been accomplished**.

It will build the components of VirtualBox. You can find the compiled binaries in `C:/VBoxBuild/VirtualBox/out/win.amd64/release/bin`.

If you've finished Step 1~5, building the binaries needs **Step 6 only**.

## Usage

### Run VirtualBox

When you run the GUI version of VirtualBox(`VirtualBox.exe`), you need dynamic libraries of both Qt and cURL library. You can run it via:

```cmd
SET PATH=%PATH%;C:\VBoxBuild\Qt\qt5-x64\bin
SET PATH=%PATH%;C:\VBoxBuild\curl\x64

C:\VBoxBuild\VirtualBox\out\win.amd64\release\bin\VirtualBox.exe
```

### Debug VirtualBox

The default setting provides disabled-hardening on the VirtualBox binary, so you can attach any kind of debugger on the running process of compiled VirtualBox.

## Bug Reporting

We use Github Issue as its primary upstream bug tracker. Bugs found when running scripts should be reported via:

- [https://github.com/VirtualBoBs/build-virtualbox-in-windows/issues](https://github.com/VirtualBoBs/build-virtualbox-in-windows/issues)

Especially, let us know if you can not download files automatically in the scripts. Old URLs in the scripts might be the causes.

## Contact

You can contact us via:

- Send a mail via a leg of bird
- Use our common telepathy
- Wish to God your genuine belief

Otherwise, you might be sued in legal ways.

## License

Copyright (c) 2020 JungHyun Kim, JaeSeung Lee of VirtualBoBs

Released under the [MIT license](https://tldrlegal.com/license/mit-license).