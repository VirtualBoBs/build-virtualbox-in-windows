url_mingw       = r'https://jaist.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win64/Personal%20Builds/rubenvb/gcc-4.5-release/x86_64-w64-mingw32-gcc-4.5.4-release-win64_rubenvb.7z'
url_sdl         = r'http://www.libsdl.org/release/SDL-devel-1.2.15-VC.zip'
url_sslx64      = r'https://slproweb.com/download/Win64OpenSSL-1_1_1h.exe'
url_sslx32      = r'https://slproweb.com/download/Win32OpenSSL-1_1_1h.exe'
url_curl        = r'https://curl.se/download/curl-7.64.1.zip'
url_qt5         = r'http://download.qt.io/new_archive/qt/5.6/5.6.3/single/qt-everywhere-opensource-src-5.6.3.zip'
url_vbox        = r'https://download.virtualbox.org/virtualbox/6.1.16/VirtualBox-6.1.16.tar.bz2'

from tool import *

def main():
    if is_admin() == False:
        print('[*] Error: Please run this script on the root privilege')
        exit(1)

    if is_test_mode() == False:
        print('[*] Error: Please run this script on the test mode')
        exit(1)

    # Create directories
    print('[+] Create directories')
    create_folder(f'{path_main_dir}/MinGW')
    create_folder(f'{path_main_dir}/SDL')
    create_folder(f'{path_main_dir}/SSL')
    create_folder(f'{path_main_dir}/curl')
    create_folder(f'{path_main_dir}/Qt')

    # Download pre-requisites
    print('[+] Set up libraries')
    print('[-] Copy SSL')
    shutil.copytree('C:/Program Files/OpenSSL-Win64', f'{path_main_dir}/SSL/OpenSSL-Win64')
    shutil.copytree('C:/Program Files (x86)/OpenSSL-Win32', f'{path_main_dir}/SSL/OpenSSL-Win32')
    print('[-] Download MinGW')
    extract_to(url_mingw, f'{path_main_dir}/MinGW', is_7z = True)
    print('[-] Download SDL')
    extract_to(url_sdl, f'{path_main_dir}/SDL')
    shutil.copytree(f'{path_main_dir}/SDL/SDL-1.2.15/include', f'{path_main_dir}/SDL/include')
    shutil.copytree(f'{path_main_dir}/SDL/SDL-1.2.15/lib/x64', f'{path_main_dir}/SDL/lib')
    print('[-] Download cURL')
    extract_to(url_curl, f'{path_main_dir}/curl')
    print('[-] Download Qt5')
    extract_to(url_qt5, f'{path_main_dir}/Qt')
    
    # Execution Part
    os.chdir(path_curr_dir)
    execute_batch_x32('build_x32.bat')
    execute_batch_x64('build_x64.bat')
    
    os.chdir(f'{path_main_dir}/Qt/qt-everywhere-opensource-src-5.6.3')
    execute_batch_x64_inst('nmake\nnmake install')
    
    os.chdir(path_curr_dir)
    # Register certification
    execute_batch_x32('build_driver.bat')

    # Configure VBox build
    execute_batch_x32('build_vbox.bat')

    # Copy local config
    os.chdir(path_vbox_dir)
    shutil.copy(f'{path_curr_dir}/LocalConfig.kmk', path_vbox_dir)

    # Build VBox
    execute_batch_x32_inst('call env.bat\nkmk')
    
    # Load drivers
    os.chdir(f'{path_vbox_dir}/out/win.amd64/release/bin')
    execute_batch_x32_inst(f'SET PATH=%PATH%;{path_main_dir}\\curl\\x64\nSET PATH=%PATH%;{path_main_dir}\\curl\\x32\ncall comregister.cmd\nloadall.cmd')

    # Execute VBox
    # execute_batch_x32_inst(f'SET PATH=%PATH%;{path_main_dir}\\Qt\\qt5-x64\\bin\nVirtualBox.exe')

main()
