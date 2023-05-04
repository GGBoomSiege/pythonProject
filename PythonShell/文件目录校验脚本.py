import os
import os.path
import hashlib
import json

def get_md5_file(md5_file):
    with open(md5_file,'r') as rfile:
        md5_str = rfile.read()
    return md5_str

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

def verify_md5(files_lst,md5_dict,new_md5_dict):
    verify_failed = []
    for file in files_lst:
        if md5_dict[file] == new_md5_dict[file]:
            continue
        else:
            print(f'文件:{file},校验不通过!')
            verify_failed.append(file)
    return verify_failed

def run(md5_file, path_dir, verify_path):
    files_lst = []

    md5_dict = json.loads(get_md5_file(md5_file))
    files_lst = get_files(path_dir, files_lst)

    new_md5_lst = get_md5(files_lst)
    new_md5_dict = {file:md5 for file,md5 in zip(files_lst,new_md5_lst)}
    verify_failed = verify_md5(files_lst,md5_dict,new_md5_dict)
    if verify_failed:
        with open(verify_path,'w') as wfile:
            for file in verify_failed:
                wfile.write(file)
                wfile.write('\n')
    else:
        print('文件校验全部通过!')

if __name__ == '__main__':
    md5_file = 'D:/test/md5.txt'
    path_dir = 'D:/test/temp'
    verify_path = 'D:/test/verify.txt'

    run(md5_file, path_dir, verify_path)


