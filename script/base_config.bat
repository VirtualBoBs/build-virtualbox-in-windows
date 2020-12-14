@echo off

SET VS2010VC_DIR=C:\Program Files (x86)\Microsoft Visual Studio 10.0
SET WINDDK_DIR=C:\WinDDK\7600.16385.1\bin\amd64

SET DEFAULT_DIR=C:\VBoxBuild

rem // Save current directory and change to target directory
pushd %DEFAULT_DIR%

rem // Save value of CD variable (current directory)
set DEFAULT_PATH=%CD%

rem // Restore original directory
popd

SET MINGW_DIR=%DEFAULT_DIR%\MinGW\mingw64
SET SDL_DIR=%DEFAULT_DIR%\SDL
SET SSL64_DIR=%DEFAULT_DIR%\SSL\OpenSSL-Win64
SET SSL32_DIR=%DEFAULT_DIR%\SSL\OpenSSL-Win32
SET CURL_DIR=%DEFAULT_DIR%\curl\curl-7.64.1
SET QT_DIR=%DEFAULT_DIR%\Qt\qt-everywhere-opensource-src-5.6.3
SET QT_BUILD_DIR=%DEFAULT_DIR%\Qt\qt5-x64
SET VBOX_DIR=%DEFAULT_DIR%\VirtualBox