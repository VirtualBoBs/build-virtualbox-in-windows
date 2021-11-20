@echo off

call base_config.bat

echo [+] cURL

echo [*] Make directories for cURL
mkdir %DEFAULT_DIR%\curl\x64\include\curl
mkdir %DEFAULT_DIR%\curl\x32\include\curl

echo [*] Build cURL x86
cd /d %CURL_DIR%\winbuild
nmake /f Makefile.vc mode=dll WITH_SSL=static DEBUG=no MACHINE=x86 SSL_PATH=%SSL32_DIR% ENABLE_SSPI=no ENABLE_WINSSL=no ENABLE_IDN=no

echo [*] Move cURL x86 files
copy ..\builds\libcurl-vc-x86-release-dll-ssl-static-ipv6\lib\libcurl.lib %DEFAULT_DIR%\curl\x32
copy ..\builds\libcurl-vc-x86-release-dll-ssl-static-ipv6\bin\libcurl.dll %DEFAULT_DIR%\curl\x32
copy ..\builds\libcurl-vc-x86-release-dll-ssl-static-ipv6\include\curl\*.h %DEFAULT_DIR%\curl\x32\include\curl

echo [*] Check moved files
IF EXIST %DEFAULT_DIR%\curl\x32\libcurl.lib echo    -libcurl.lib OK
IF EXIST %DEFAULT_DIR%\curl\x32\libcurl.dll echo    -libcurl.dll OK
IF EXIST %DEFAULT_DIR%\curl\x32\include echo    -Include Files OK

echo [*] Clean
nmake /f Makefile.vc mode=dll clean
