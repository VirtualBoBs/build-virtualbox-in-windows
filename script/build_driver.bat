@echo off

call base_config.bat

echo [+]Certification
cd %VBOX_DIR%
set PATH=%PATH%;%WINDDK_DIR%;

echo [-]MyTestCertificate Make
makecert.exe -r -pe -ss my -eku 1.3.6.1.5.5.7.3.3 -n "CN=MyTestCertificate" mytestcert.cer

echo [-]certmgr to root, trustedpublisher
certmgr.exe -add mytestcert.cer -s -r localMachine root
certmgr.exe -add mytestcert.cer -s -r localMachine trustedpublisher

echo [+]Certification Job Finished
