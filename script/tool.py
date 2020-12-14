import subprocess
from urllib import request
import zipfile
import os, shutil
import ctypes
from subprocess import Popen, PIPE

path_prompt_x32 = r'C:\"Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\vcvars32.bat"'
path_prompt_x64 = r'C:\"Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\amd64\vcvars64.bat"'

def get_working_path():
    return os.path.dirname(os.path.abspath(__file__))

def is_admin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def is_test_mode():
    l = 'bcdedit /v'.split(' ')
    key = 'testsigning             '

    process = Popen(l, stdout=PIPE)
    (output, err) = process.communicate()
    
    output = str(output)

    idx = output.find(key)
    if idx == -1:
        is_test_mode = False
    else:
        output = output[output.find(key) + len(key):]
        is_test_mode = output.startswith('Yes')
    return is_test_mode

# Return false when the directory already exists.
def create_folder(dir):
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except OSError:
            print(f'[*] Error: Could not create the directory {dir}')
            exit(1)
        return True
    return False

def generate_temp_file_name():
    return 'temp.bin'

def generate_temp_bat_name():
    return 'temp.bat'

def extract_to(url, path, internal = False):
    temp_path = generate_temp_file_name()
    request.urlretrieve(url, temp_path)

    if internal:
        with zipfile.ZipFile(temp_path) as f:
            f.extractall(path)
    else:
        unzip_path = os.path.abspath('../bin/7za/7za')
        instruction = f'{unzip_path} x {temp_path} -o{path}'
        os.system(instruction)
    
    os.remove(temp_path)

def execute_batch_x32_inst(inst):
    temp_bat_path = generate_temp_bat_name()
    with open(temp_bat_path, 'wt') as f:
        f.write(f'call {path_prompt_x32}\n')
        f.write(f'{inst}\n')      
    subprocess.call([temp_bat_path])
    os.remove(temp_bat_path)

def execute_batch_x32(path):
    execute_batch_x32_inst(f'call {path}')
    
def execute_batch_x64_inst(inst):
    temp_bat_path = generate_temp_bat_name()
    with open(temp_bat_path, 'wt') as f:
        f.write(f'call {path_prompt_x64}\n')
        f.write(f'{inst}\n')      
    subprocess.call([temp_bat_path])
    os.remove(temp_bat_path)

def execute_batch_x64(path):
    execute_batch_x64_inst(f'call {path}')

path_curr_dir   = get_working_path()
path_main_dir   = os.path.abspath(f'{path_curr_dir}/../bin')
path_vbox_dir   = os.path.abspath(f'{path_main_dir}/VirtualBox')