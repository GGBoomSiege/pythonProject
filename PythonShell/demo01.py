from pykeyboard import PyKeyboard
from pymouse import PyMouse
import win32gui
import win32con
import operator
import datetime

import os
import os.path
import hashlib

def get_files(dir_path, list_name):
    for file in os.listdir(dir_path):
        file_path = '/'.join([dir_path,file])
        if os.path.isdir(file_path):
            get_files(file_path, list_name)
        else:
            list_name.append(file_path)
    return list_name

if __name__ == '__main__':
    # handle = win32gui.FindWindow("Notepad", "记事本")
    # win32gui.SetForegroundWindow(handle)
    # win32gui.ShowWindow(handle, win32con.SW_SHOW)
    # path_dir = 'D:/test/out.txt'
    # print(path_dir.split('/')[0:2])
    # temp_str = '/'.join([path_dir.split('/')[0:2], 'update'])
    # print(temp_str)
    # for i in range(11):
    #     # os.mkdir('/'.join(['D:/test/temp',str(i)]))
    #     with open('/'.join(['D:/test/temp',str(i),str(i)+'.txt']),'w') as wfile:
    #         wfile.write(str(i))
    # lst = []
    # print(get_files('D:/test/temp',lst))
    file = 'D:/test/temp/7/7.txt'

    with open(file,'r') as rfile:
        print(hashlib.md5(rfile.read().encode('utf-8')).hexdigest())