import os
import os.path
import hashlib
import json

def get_files(path_dir, list_name):
    for file in os.listdir(path_dir):
        file_path = '/'.join([path_dir, file])
        if os.path.isdir(file_path):
            get_files(file_path, list_name)
        else:
            list_name.append(file_path)
    return list_name

def get_md5(files_lst):
    md5_lst = []
    for i in files_lst:
        with open(i,'r') as rfile:
            '''此处不要新建hashlib对象，会引起md5值失真。'''
            md5_lst.append(hashlib.md5(rfile.read().encode('utf-8')).hexdigest())
    return md5_lst

def save_to_file(md5_str, path_file):
    with open(path_file,'w') as wfile:
        wfile.write(md5_str)

if __name__ == '__main__':
    path_dir = 'D:/test/temp'
    path_file = 'D:/test/md5.txt'

    files_lst = []

    files_lst = get_files(path_dir, files_lst)
    md5_lst = get_md5(files_lst)
    md5_dict = {file:md5 for file,md5 in zip(files_lst,md5_lst)}

    try:
        save_to_file(json.dumps(md5_dict), path_file)
    except Exception as e:
        print(e)
    else:
        print(f'MD5校验值收集成功,收集文件地址为:{path_file}')