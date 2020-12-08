url_mingw       = r'https://jaist.dl.sourceforge.net/project/mingw-w64/mingw-w64/mingw-w64-release/mingw-w64-v8.0.0.zip'
url_sdl         = r'http://www.libsdl.org/release/SDL-devel-1.2.15-VC.zip'
url_sslx64      = r'https://slproweb.com/download/Win64OpenSSL-1_1_1h.exe'
url_sslx32      = r'https://slproweb.com/download/Win32OpenSSL-1_1_1h.exe'
url_curl        = r'https://curl.se/download/curl-7.64.1.zip'
url_qt5         = r'http://download.qt.io/new_archive/qt/5.6/5.6.3/single/qt-everywhere-opensource-src-5.6.3.zip'
url_vbox        = r'https://download.virtualbox.org/virtualbox/6.1.16/VirtualBox-6.1.16.tar.bz2'

path_prompt_x32 = r'C:\"Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\vcvars32.bat"'
path_prompt_x64 = r'C:\"Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\amd64\vcvars64.bat"'
path_main_dir = r'C:\VBoxCompile'

import subprocess
from urllib import request
import zipfile
import os, shutil

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
    # Make Directories
    print('[+] Making Directories')
    print('[-] MinGW Directory')
    createFolder(path_main_dir+'/MinGW')
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
    print('[+] Install Required Programs')
    print('[-] Install MinGW')
    extract_to(url_mingw, path_main_dir+'/MinGW')

    print('[-] Install SDL')
    extract_to(url_sdl, './')
    shutil.copytree('./include',path_main_dir+'/SDL/include')
    shutil.copytree('./lib/x64',path_main_dir+'/SDL/lib')

    print('[-] Install SSLs')
    # you should run url_sslx64,x32 before these command starts
    shutil.copytree('C:/Program Files/OpenSSL-Win64',path_main_dir+'/SSL/x64')
    shutil.copytree('C:/Program Files (x86)/OpenSSL-Win32',path_main_dir+'/SSL/x32')

    print('[-] Install cURL')
    extract_to(url_curl, path_main_dir+'/curl')

    print('[-] Install qt5')
    extract_to(url_qt5, path_main_dir+'/Qt')

    print('[-] Install VirtualBox')
    extract_to(url_vbox, path_main_dir)

    # Execution Part
    os.chdir(path_main_dir+'/scripts')
    execute_batch_x32(r'buildx32.bat')
    execute_batch_x64(r'buildx64.bat')
    os.chdir(path_main_dir+'/Qt/qt-everywhere-opensource-src-5.6.3')
    execute_batch_x64_inst(r'nmake\n nmake install')
    os.chdir(path_main_dir+'/scripts')
    execute_batch_x32(r'build_driver.bat\n build_vbox.bat')
    os.chdir(path_main_dir+'/VirtualBox-6.1.16')
    execute_batch_x32_inst(r'env.bat\n kmk')
    os.chdir(path_main_dir+'/VirtualBox-6.1.16/out/win.amd64/release/bin')
    execute_batch_x32_inst(r'SET PATH=%PATH%;'+path_main_dir+r'\curl\x64 \n SET PATH=%PATH%;'+path_main_dir+r'\curl\x32')

    # admin privillege needs
    execute_batch_x32(r'comregister.cmd\n loadall.cmd')

    execute_batch_x32(r'SET PATH=%PATH%;'+path_main_dir+r'\Qt\qt5-x64\bin \n VirtualBox.exe')

main()
