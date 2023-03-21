import os.path

if __name__ == '__main__':
        filename='D:\\opcloud\\iot\\data-transmit-0.0.1-SNAPSHOT.jar'
        if os.path.exists(filename):
            print('yes')
        else:
            print('no')
