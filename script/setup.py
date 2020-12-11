url_mingw       = r'https://jaist.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win64/Personal%20Builds/rubenvb/gcc-4.5-release/x86_64-w64-mingw32-gcc-4.5.4-release-win64_rubenvb.7z'
url_sdl         = r'http://www.libsdl.org/release/SDL-devel-1.2.15-VC.zip'
url_sslx64      = r'https://slproweb.com/download/Win64OpenSSL-1_1_1h.exe'
url_sslx32      = r'https://slproweb.com/download/Win32OpenSSL-1_1_1h.exe'
url_curl        = r'https://curl.se/download/curl-7.64.1.zip'
url_qt5         = r'http://download.qt.io/new_archive/qt/5.6/5.6.3/single/qt-everywhere-opensource-src-5.6.3.zip'
url_vbox        = r'https://download.virtualbox.org/virtualbox/6.1.16/VirtualBox-6.1.16.tar.bz2'

path_prompt_x32 = r'C:\"Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\vcvars32.bat"'
path_prompt_x64 = r'C:\"Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\amd64\vcvars64.bat"'
path_main_dir   = r'C:\VBoxCompile'
path_vbox_dir   = r'C:\VBoxCompile\VirtualBox-6.1.16' # you should install this first and input directory.

import subprocess
from urllib import request
import zipfile
import os, shutil
import ctypes

def is_admin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def createFolder(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print('[*] Error: Creating directory '+dir+'. It is already exist')

def generate_temp_name():
    return 'temp.bin'

def generate_temp_bat_name():
    return 'temp.bat'

def extract_to(url, path):
    temp_path = generate_temp_name()
    request.urlretrieve(url, temp_path)

    f = zipfile.ZipFile(temp_path)
    f.extractall(path)
    f.close()

def execute_batch_x32(path):
    temp_bat_path = generate_temp_bat_name()
    with open(temp_bat_path, 'wt') as f:
        f.write(f'call {path_prompt_x32}\n')
        f.write(f'call {path}\n')      
    subprocess.call([temp_bat_path])
    
def execute_batch_x64(path):
    temp_bat_path = generate_temp_bat_name()
    with open(temp_bat_path, 'wt') as f:
        f.write(f'call {path_prompt_x64}\n')
        f.write(f'call {path}\n')      
    subprocess.call([temp_bat_path])

def execute_batch_x32_inst(inst):
    temp_bat_path = generate_temp_bat_name()
    with open(temp_bat_path, 'wt') as f:
        f.write(f'call {path_prompt_x32}\n')
        f.write(f'{inst}\n')      
    subprocess.call([temp_bat_path])
    
def execute_batch_x64_inst(inst):
    temp_bat_path = generate_temp_bat_name()
    with open(temp_bat_path, 'wt') as f:
        f.write(f'call {path_prompt_x64}\n')
        f.write(f'{inst}\n')      
    subprocess.call([temp_bat_path])

def main():
    if is_admin() == False:
        print('[+] Please run this script on root')
        return

    # Make Directories
    print('[+] Making Directories')
    #print('[-] MinGW Directory')
    #createFolder(path_main_dir+'/MinGW')
    print('[-] SDL Directory')
    createFolder(path_main_dir+'/SDL')
    print('[-] SSL Directory')
    createFolder(path_main_dir+'/SSL')
    print('[-] curl Directory')
    createFolder(path_main_dir+'/curl')
    print('[-] Qt Directory')
    createFolder(path_main_dir+'/Qt')
    print('[+] Making Directories Done')

    # Installation Part
    #print('[+] Install Required Programs')
    #print('[-] Install MinGW')
    #extract_to(url_mingw, path_main_dir+'/MinGW')
    
    print('[-] Install SDL')
    extract_to(url_sdl, path_main_dir+'/SDL')
    shutil.copytree(path_main_dir+'/SDL/SDL-1.2.15/include',path_main_dir+'/SDL/include')
    shutil.copytree(path_main_dir+'/SDL/SDL-1.2.15/lib/x64',path_main_dir+'/SDL/lib')

    print('[-] Install SSLs')
    # you should run url_sslx64,x32 before these command starts
    shutil.copytree('C:/Program Files/OpenSSL-Win64',path_main_dir+'/SSL/OpenSSL-Win64')
    shutil.copytree('C:/Program Files (x86)/OpenSSL-Win32',path_main_dir+'/SSL/OpenSSL-Win32')

    print('[-] Install cURL')
    extract_to(url_curl, path_main_dir+'/curl')

    print('[-] Install qt5 (It will take a long long time. Be Patience.)')
    extract_to(url_qt5, path_main_dir+'/Qt')
    print('[+] Install Required Programs Done')
    
    # Execution Part
    os.chdir(path_main_dir+'/scripts')
    execute_batch_x32(r'buildx32.bat')
    execute_batch_x64(r'buildx64.bat')
    
    os.chdir(path_main_dir+'/Qt/qt-everywhere-opensource-src-5.6.3')
    execute_batch_x64_inst(r'nmake')
    execute_batch_x64_inst(r'nmake install')
    os.chdir(path_main_dir+'/scripts')
    execute_batch_x32(r'build_driver.bat')
    
    execute_batch_x32(r'build_vbox.bat')
    os.chdir(path_vbox_dir)
    shutil.copy(path_main_dir+'/scripts/LocalConfig.kmk',path_vbox_dir)
    execute_batch_x32_inst('call env.bat\nkmk')
    
    os.chdir(path_vbox_dir+'/out/win.amd64/release/bin')
    execute_batch_x32_inst('call SET PATH=%PATH%;'+path_main_dir+r'\curl\x64\nSET PATH=%PATH%;'+path_main_dir+r'\curl\x32\ncall comregister.cmd\nloadall.cmd\ncall SET PATH=%PATH%;'+path_main_dir+'\Qt\qt5-x64\bin\nVirtualBox.exe')

main()
