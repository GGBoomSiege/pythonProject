import uuid
import datetime
def unique_id():
    unique_id_lst = [datetime.datetime.now().strftime('%Y%m%d'), str(uuid.uuid4().int % (10 ** 8))]
    unique_id = int(''.join(unique_id_lst))
    return unique_id

if __name__ == '__main__':
    print(unique_id())