import os
import magic
import re
import codecs

def is_binary_file_1(ff):

    TEXT_BOMS = (
        codecs.BOM_UTF16_BE,
        codecs.BOM_UTF16_LE,
        codecs.BOM_UTF32_BE,
        codecs.BOM_UTF32_LE,
        codecs.BOM_UTF8,
    )
    with open(ff, 'rb') as file:
        CHUNKSIZE = 8192
        initial_bytes = file.read(CHUNKSIZE)
        file.close()
    #: BOMs to indicate that a file is a text file even if it contains zero bytes.
    return not any(initial_bytes.startswith(bom) for bom in TEXT_BOMS) and b'\0' in initial_bytes


def is_binwary_file_2(ff):
    mime_kw = 'x-executable|x-sharedlib|octet-stream|x-object'  ###可执行文件、链接库、动态流、对象
    try:
        magic_mime = magic.from_file(ff, mime=True)
        magic_hit = re.search(mime_kw, magic_mime, re.I)
        if magic_hit:
            return True
        else:
            return False
    except Exception as e:
        return False

class Ftp:
    def __init__(self,filename):
        self.filename=filename

    def get(self):
        file_list1=['file_size','file_type','file_data']
        file_list2=[]
        if any((is_binary_file_1(self.filename), is_binwary_file_2(self.filename))):
            with open(self.filename,'rb') as rfile:
                data=rfile.read()
                file_list2.append(len(data))
                file_list2.append(str(type(data)))
                file_list2.append(data)
                file_dict={file_list1:file_list2 for file_list1,file_list2 in zip(file_list1,file_list2)}
                return file_dict
        else:
            with open(self.filename,'r',encoding='utf-8') as rfile:
                data = rfile.read()
                file_list2.append(len(data))
                file_list2.append(str(type(data)))
                file_list2.append(data)
                file_dict = {file_list1: file_list2 for file_list1, file_list2 in zip(file_list1, file_list2)}
                return file_dict

    def put(self):
        pass

if __name__ == "__main__":
    file_path = "D:\\opcloud\\minio\\data\\default\\2f229807-ab30-472c-917d-dc48a9b4cde0.png"
    ftpSample=Ftp(file_path)
    var=ftpSample.get()
    print(var)
