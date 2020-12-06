url_mingw       = r'https://jaist.dl.sourceforge.net/project/mingw-w64/mingw-w64/mingw-w64-release/mingw-w64-v8.0.0.zip'
url_sdl         = r'http://www.libsdl.org/release/SDL-devel-1.2.15-VC.zip'

path_prompt_x32 = r'C:\"Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\vcvars32.bat"'
path_prompt_x64 = r'C:\"Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\amd64\vcvars64.bat"'

import subprocess
from urllib import request
import zipfile

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
    with open(generate_temp_bat_name(), 'wt') as f:
        f.write(f'call {path_prompt_x32}\n')
        f.write(f'call {path}\n')      
    subprocess.call([temp_bat_path])
    
def execute_batch_x64(path):
    temp_bat_path = generate_temp_bat_name()
    with open(generate_temp_bat_name(), 'wt') as f:
        f.write(f'call {path_prompt_x64}\n')
        f.write(f'call {path}\n')      
    subprocess.call([temp_bat_path])

def main():
    # Installation Part
    print('[*] Install MinGW')
    extract_to(url_mingw, './')

    print('[*] Install SDL')
    extract_to(url_sdl, './')

    # Execution Part
    execute_batch_x32(r'buildx32.bat')

main()