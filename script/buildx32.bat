@echo off

echo [+]Initialization(You must need to Check these directories)
SET DEFAULT_DIR=C:\VBoxCompile
SET SSL32_DIR=C:\VBoxCompile\SSL\OpenSSL-Win32
SET CURL_DIR=C:\VBoxCompile\curl\curl-7.64.1

:: Run this build.bat in Visual Studio Command Prompt (2010) in Administrator

:: CURL x32,x64 Compile
echo [+]cURL

echo [-]cURL Initialization
mkdir %DEFAULT_DIR%\curl\x64\include\curl
mkdir %DEFAULT_DIR%\curl\x32\include\curl
cd %CURL_DIR%

echo [*]cURL x86 Build
cd /d winbuild
nmake /f Makefile.vc mode=dll WITH_SSL=static DEBUG=no MACHINE=x86 SSL_PATH=%SSL32_DIR% ENABLE_SSPI=no ENABLE_WINSSL=no ENABLE_IDN=no

echo [*]cURL x86 Files Move
copy ..\builds\libcurl-vc-x86-release-dll-ssl-static-ipv6\lib\libcurl.lib %DEFAULT_DIR%\curl\x32
copy ..\builds\libcurl-vc-x86-release-dll-ssl-static-ipv6\bin\libcurl.dll %DEFAULT_DIR%\curl\x32
copy ..\builds\libcurl-vc-x86-release-dll-ssl-static-ipv6\include\curl\*.h %DEFAULT_DIR%\curl\x32\include\curl

echo [*]Check Moving Files
IF EXIST %DEFAULT_DIR%\curl\x32\libcurl.lib echo    -libcurl.lib OK
IF EXIST %DEFAULT_DIR%\curl\x32\libcurl.dll echo    -libcurl.dll OK
IF EXIST %DEFAULT_DIR%\curl\x32\include echo    -Include Files OK

echo [-]Cleaning...
nmake /f Makefile.vc mode=dll clean
