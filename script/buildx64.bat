@echo off

echo [+]Initialization(You must need to Check these directories)
SET DEFAULT_DIR=C:\VBoxCompile
SET SSL64_DIR=C:\VBoxCompile\SSL\OpenSSL-Win64
SET CURL_DIR=C:\VBoxCompile\curl\curl-7.64.1
SET QT_DIR=C:\VBoxCompile\Qt\qt-everywhere-opensource-src-5.6.3

echo [+]cURL

echo [-]cURL x64

echo [*]cURL x64 Build
cd /d %CURL_DIR%\winbuild
nmake /f Makefile.vc mode=dll WITH_SSL=static DEBUG=no MACHINE=x64 SSL_PATH=%SSL64_DIR% ENABLE_SSPI=no ENABLE_WINSSL=no ENABLE_IDN=no

echo [*]cURL x64 Files Move
copy ..\builds\libcurl-vc-x64-release-dll-ssl-static-ipv6\lib\libcurl.lib %DEFAULT_DIR%\curl\x64
copy ..\builds\libcurl-vc-x64-release-dll-ssl-static-ipv6\bin\libcurl.dll %DEFAULT_DIR%\curl\x64
copy ..\builds\libcurl-vc-x64-release-dll-ssl-static-ipv6\include\curl\*.h %DEFAULT_DIR%\curl\x64\include\curl

echo [*]Check Moving Files
IF EXIST %DEFAULT_DIR%\curl\x64\libcurl.lib echo    -libcurl.lib OK
IF EXIST %DEFAULT_DIR%\curl\x64\libcurl.dll echo    -libcurl.dll OK
IF EXIST %DEFAULT_DIR%\curl\x64\include echo    -Include Files OK

echo [+]cURL Job Finished

::Qt Compile
echo [+]Qt
echo [-]Qt x64 Build Setting
cd %QT_DIR%
configure.bat -opensource -confirm-license -nomake tests -nomake examples -no-compile-examples -release -shared -no-ltcg -accessibility -no-sql-sqlite -opengl desktop -no-openvg -no-nis -no-iconv -no-evdev -no-mtdev -no-inotify -no-eventfd -largefile -no-system-proxies -qt-zlib -qt-pcre -no-icu -qt-libpng -qt-libjpeg -qt-freetype -no-fontconfig -qt-harfbuzz -no-angle -incredibuild-xge -no-plugin-manifests -qmake -qreal double -rtti -strip -no-ssl -no-openssl -no-libproxy -no-dbus -no-audio-backend -no-wmf-backend -no-qml-debug -no-direct2d -directwrite -no-style-fusion -native-gestures -skip qt3d -skip qtactiveqt -skip qtandroidextras -skip qtcanvas3d -skip qtconnectivity -skip qtdeclarative -skip qtdoc -skip qtenginio -skip qtgraphicaleffects -skip qtlocation -skip qtmacextras -skip qtmultimedia -skip qtquickcontrols -skip qtquickcontrols2 -skip qtscript -skip qtsensors -skip qtserialbus -skip qtserialport -skip qtwayland -skip qtwebchannel -skip qtwebengine -skip qtwebsockets -skip qtwebview -skip qtx11extras -skip qtxmlpatterns -prefix %DEFAULT_DIR%\Qt\qt5-x64

echo [+]buildx64.bat finished. Type nmake, nmake install in C:\VBoxCompile\Qt\qt-everywhere-opensource-src-5.6.3 with Visual Studio x64 Win64 Command Prompt (2010).