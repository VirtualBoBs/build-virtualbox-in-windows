@echo off

echo [+]Initialization(You must need to Check these directories)
SET DEFAULT_DIR=C:\VBoxCompile
SET VS2010VC_DIR=C:\Program Files (x86)\Microsoft Visual Studio 10.0
SET WINDDK_DIR=C:\WinDDK\7600.16385.1\bin\amd64
SET MINGW_DIR=C:\VBoxCompile\MinGW\mingw64
SET SDL_DIR=C:\VBoxCompile\SDL
SET SSL64_DIR=C:\VBoxCompile\SSL\OpenSSL-Win64
SET SSL32_DIR=C:\VBoxCompile\SSL\OpenSSL-Win32
SET CURL_DIR=C:\VBoxCompile\curl\curl-7.64.1
SET QT_DIR=C:\VBoxCompile\Qt\qt-everywhere-opensource-src-5.6.3
SET VBOX_DIR=C:\VBoxCompile\VirtualBox-6.1.16
SET QT_BUILD_DIR=%DEFAULT_DIR%\Qt\qt5-x64

::VirtualBox Build
echo [+]VirtualBox
cd /d %VBOX_DIR%

echo  [-]VirtualBox Build Setting
set BUILD_TARGET_ARCH=amd64
cscript configure.vbs --with-vc="%VS2010VC_DIR%" --with-qt5="%DEFAULT_DIR%\Qt\qt5-x64" --with-DDK="%WINDDK_DIR%" --with-MinGW-w64="%MINGW_DIR%" --with-libSDL="%SDL_DIR%" --with-openssl="%SSL64_DIR%" --with-openssl32="%SSL32_DIR%" --with-libcurl="%DEFAULT_DIR%\curl\x64" --with-libcurl32="%DEFAULT_DIR%\curl\x32"