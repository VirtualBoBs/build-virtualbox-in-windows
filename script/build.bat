:: Copyright 2020, VirtualBoBs All Rights Reserved
:: Every Files (except Microsoft Visual Studio 2010, Service Pack, SDKs) must be in C:\VBoxCompile
:: ENV SET : Safe Boot Off, Windows Test Mode ON, Visual Studio Command Prompt (2010)
:: Bcdedit.exe -set TESTSIGNING ON
:: Need Directory List
:: C:\VBoxCompile\
::		  MinGW\mingw64,
::		  SDL\SDL-1.2.15
::		  SSL\x64,x32
::		  curl\curl-7.64.1
::		  VirtualBox-6.1.16
::		  Qt\qt5-x64,qt-everywhere-opensource-src-5.6.3

@echo off

echo [+]Initialization(You must need to Check this directories)
SET DEFAULT_DIR=C:\VBoxCompile
SET VS2010VC_DIR=C:\Program Files (x86)\Microsoft Visual Studio 10.0
SET WINDDK_DIR=C:\WinDDK\7600.16385.1\bin\amd64
SET MINGW_DIR=C:\VBoxCompile\MinGW\mingw64
SET SDL_DIR=C:\VBoxCompile\SDL
SET SSL64_DIR=C:\VBoxCompile\SSL\x64
SET SSL32_DIR=C:\VBoxCompile\SSL\x32
SET CURL_DIR=C:\VBoxCompile\curl\curl-7.64.1
SET QT_DIR=C:\VBoxCompile\Qt\qt-everywhere-opensource-src-5.6.3
SET VBOX_DIR=C:\VBoxCompile\VirtualBox-6.1.16

:: Run this build.bat in Visual Studio Command Prompt (2010) in Administrator

:: CURL x32,x64 Compile
echo [+]cURL

echo  [-]cURL Initialization
mkdir %CURL_DIR%\x64\include
mkdir %CURL_DIR%\x32\include
cd %CURL_DIR%

echo   [*]cURL x64 Build
"C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.Cmd" /Release /x64 /win7
COLOR 07
cd /d winbuild
nmake /f Makefile.vc mode=dll WITH_SSL=static DEBUG=no MACHINE=x64 SSL_PATH=%SSL64_DIR% ENABLE_SSPI=no ENABLE_WINSSL=no ENABLE_IDN=no

echo   [*]cURL x64 Files Move
copy ..\builds\libcurl-vc-x64-release-dll-ssl-static-ipv6\lib\libcurl.lib %CURL_DIR%\x64
copy ..\builds\libcurl-vc-x64-release-dll-ssl-static-ipv6\bin\libcurl.dll %CURL_DIR%\x64
copy ..\builds\libcurl-vc-x64-release-dll-ssl-static-ipv6\include\* %CURL_DIR%\x64\include

echo   [*]Check Moving Files
IF EXIST %CURL_DIR%\x64\libcurl.lib echo    -libcurl.lib OK
IF EXIST %CURL_DIR%\x64\libcurl.dll echo    -libcurl.dll OK
IF EXIST %CURL_DIR%\x64\include echo    -Include Files OK

echo  [-]Cleaning...
nmake /f Makefile.vc mode=dll clean

echo   [*]cURL x86 Build
"C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.Cmd" /Release /x86 /win7
COLOR 07
nmake /f Makefile.vc mode=dll WITH_SSL=static DEBUG=no MACHINE=x86 SSL_PATH=%SSL32_DIR% ENABLE_SSPI=no ENABLE_WINSSL=no ENABLE_IDN=no

echo   [*]cURL x86 Files Move
copy ..\builds\libcurl-vc-x86-release-dll-ssl-static-ipv6\lib\libcurl.lib %CURL_DIR%\x32
copy ..\builds\libcurl-vc-x86-release-dll-ssl-static-ipv6\bin\libcurl.dll %CURL_DIR%\x32
copy ..\builds\libcurl-vc-x86-release-dll-ssl-static-ipv6\include\* %CURL_DIR%\x32\include

echo   [*]Check Moving Files
IF EXIST %CURL_DIR%\x32\libcurl.lib echo    -libcurl.lib OK
IF EXIST %CURL_DIR%\x32\libcurl.dll echo    -libcurl.dll OK
IF EXIST %CURL_DIR%\x32\include echo    -Include Files OK

echo [+]cURL Job Finished

::Qt Compile
echo [+]Qt
echo  [-]Qt x64 Build Setting
cd %QT_DIR%
"C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.Cmd" /Release /x64 /win7
color 07
configure.bat -opensource -confirm-license -nomake tests -nomake examples -no-compile-examples -release -shared -no-ltcg -accessibility -no-sql-sqlite -opengl desktop -no-openvg -no-nis -no-iconv -no-evdev -no-mtdev -no-inotify -no-eventfd -largefile -no-system-proxies -qt-zlib -qt-pcre -no-icu -qt-libpng -qt-libjpeg -qt-freetype -no-fontconfig -qt-harfbuzz -no-angle -incredibuild-xge -no-plugin-manifests -qmake -qreal double -rtti -strip -no-ssl -no-openssl -no-libproxy -no-dbus -no-audio-backend -no-wmf-backend -no-qml-debug -no-direct2d -directwrite -no-style-fusion -native-gestures -skip qt3d -skip qtactiveqt -skip qtandroidextras -skip qtcanvas3d -skip qtconnectivity -skip qtdeclarative -skip qtdoc -skip qtenginio -skip qtgraphicaleffects -skip qtlocation -skip qtmacextras -skip qtmultimedia -skip qtquickcontrols -skip qtquickcontrols2 -skip qtscript -skip qtsensors -skip qtserialbus -skip qtserialport -skip qtwayland -skip qtwebchannel -skip qtwebengine -skip qtwebsockets -skip qtwebview -skip qtx11extras -skip qtxmlpatterns -prefix %QT_DIR%\qt5-x64

echo  [-]Qt Build Start (It will take long time)
nmake
nmake install

SET QT_BUILD_DIR=%QT_DIR%\qt5-x64

echo [+]Qt Job Finished

::make mycert
echo [+]Certification
cd %VBOX_DIR%
set PATH=%PATH%;%WINDDK_DIR%;

echo  [-]MyTestCertificate Make
makecert.exe -r -pe -ss my -eku 1.3.6.1.5.5.7.3.3 -n "CN=MyTestCertificate" mytestcert.cer

echo  [-]certmgr to root, trustedpublisher
certmgr.exe -add mytestcert.cer -s -r localMachine root
certmgr.exe -add mytestcert.cer -s -r localMachine trustedpublisher

echo [+]Certification Job Finished

::VirtualBox Build
echo [+]VirtualBox
cd %VBox_DIR%

echo  [-]VirtualBox Build Setting
set BUILD_TARGET_ARCH=amd64
cscript configure.vbs --with-vc=%VS2010VC_DIR% --with-qt5=%QT_BUILD_DIR% --with-DDK="C:/WinDDK/7600.16385.1" --with-MinGW-w64="C:/VBoxCompile/MinGW/mingw64" --with-libSDL="C:/VBoxCompile/SDL" --with-openssl="C:/VBoxCompile/SSL/x64" --with-openssl32="C:/VBoxCompile/SSL\x32" --with-libcurl="C:/VBoxCompile/curl/x64" --with-libcurl32="C:/VBoxCompile/curl/x32"

echo  [-]VirtualBox Build Start (It will take long time)
env.bat
kmk

echo  [-]VirtualBox Build Finished
cd %VBOX_DIR%\out\win.amd64\release\bin

set PATH=%PATH%;%DEFAULT_DIR%\curl\x32;
set PATH=%PATH%;%DEFAULT_DIR%\curl\x64;

echo  [-]Driver Register and Setting
comregister.cmd
loadall.cmd

echo [+]VirtualBox Job Finished

echo [+]Build Finished. You MUST insert System Path about qt5-x64\bin,curl x32,curl x64. And then VirtualBox.exe Run.

:: finally you need to PATH C:\VBoxCompile\Qt\qt5-x64\bin, C:\VBoxCompile\curl\x32, C:\VBoxCompile\curl\x64
