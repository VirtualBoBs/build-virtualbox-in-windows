from tool import *

def main():
    # Build VBox
    os.chdir(path_vbox_dir)
    execute_batch_x32_inst('call env.bat\nkmk')
    
    # Load drivers
    os.chdir(f'{path_vbox_dir}/out/win.amd64/release/bin')
    execute_batch_x32_inst(f'SET PATH=%PATH%;{path_main_dir}\\curl\\x64\nSET PATH=%PATH%;{path_main_dir}\\curl\\x32\ncall comregister.cmd\nloadall.cmd')

    # Execute VBox
    # execute_batch_x32_inst(f'SET PATH=%PATH%;{path_main_dir}\\Qt\\qt5-x64\\bin\nVirtualBox.exe')

if __name__ == '__main__':
    main()