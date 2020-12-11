@echo off

call base_config.bat

::VirtualBox Build
echo [+]VirtualBox
cd /d %VBOX_DIR%

echo [-]VirtualBox Build Setting
set BUILD_TARGET_ARCH=amd64
cscript configure.vbs --with-vc="%VS2010VC_DIR%" --with-qt5="%DEFAULT_DIR%\Qt\qt5-x64" --with-DDK="%WINDDK_DIR%" --with-MinGW-w64="%MINGW_DIR%" --with-libSDL="%SDL_DIR%" --with-openssl="%SSL64_DIR%" --with-openssl32="%SSL32_DIR%" --with-libcurl="%DEFAULT_DIR%\curl\x64" --with-libcurl32="%DEFAULT_DIR%\curl\x32"


echo [+]VirtualBox Build Setting Done
