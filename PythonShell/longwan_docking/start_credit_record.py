# -*- coding:utf-8 -*-
from common.mysql_operate import *
from config.setting import *
import requests
import json
import time


class Crawl(object):
    def __init__(self):
        self.url_1 = (
            "https://api-dshare.wenzhou.gov.cn/webapi2/LW-xysh__enterprise_label"
        )
        self.url_2 = "https://api-dshare.wenzhou.gov.cn/webapi2/LW-wz_hj_biz_0300_xysh__credit_record_valid_old"
        self.url_3 = "https://api-dshare.wenzhou.gov.cn/webapi2/LW-wz_hj_biz_0300_xysh__enterprise_credit_valid_old"

        self.header = {"Authorization": ""}
        self.payload = {"powermatters": "", "subpowermatters": "", "p_credit_code": ""}

    def gettoken(self):
        url_token = "https://api-dshare.wenzhou.gov.cn/webapi2/get_token"
        payload = {
            "username": "wll.wqqy",
            "password": "b2f89c71-99f5-4a09-95d5-40770e2f2424",
        }
        response = requests.post(url=url_token, json=payload)
        token = json.loads(response.text)["token"]
        return token

    def start_credit_record(self):
        token = self.gettoken()
        print(token)
        Authorization = "jwt " + token
        self.header["Authorization"] = Authorization
        print(self.header)

        uscc_list = dbo_ydb.select_all(
            "select * from dcv3_sdata_dir_eplist where extmark is null"
        )
        for item in uscc_list:
            uscc = item["uscc"]
            if not uscc:
                continue
            self.payload["p_credit_code"] = uscc
            print(self.payload)
            response = requests.post(
                url=self.url_2, headers=self.header, json=self.payload
            )
            print(response.text)
            result = json.loads(response.text)
            if "error" in result:
                error = result["error"]
                if error == "签名已过期":
                    token = self.gettoken()
                    print(token)
                    Authorization = "jwt " + token
                    self.header["Authorization"] = Authorization
                    self.payload["p_credit_code"] = uscc
                    response = requests.post(
                        url=self.url_2, headers=self.header, json=self.payload
                    )
            josn_items = json.loads(response.text)["datas"]

            if not josn_items:
                continue

            for item in josn_items:
                ID = item["ID"]
                DATE_A = item["DATE_A"]
                DEPARTMENT_ID = item["DEPARTMENT_ID"]
                CREDIT_CODE = item["CREDIT_CODE"]
                FIRST_ITEM_ID = item["FIRST_ITEM_ID"]
                SECOND_ITEM_ID = item["SECOND_ITEM_ID"]
                CREDIT_RECORD_TYPE = item["CREDIT_RECORD_TYPE"]
                NOW_SCORE = item["NOW_SCORE"]
                ORIGINAL_SCORE = item["ORIGINAL_SCORE"]
                NOW_TOTAL_SCORE = item["NOW_TOTAL_SCORE"]
                ORIGINAL_TOTAL_SCORE = item["ORIGINAL_TOTAL_SCORE"]
                RETURN_SCORE = item["RETURN_SCORE"]
                SCORE_TYPE = item["SCORE_TYPE"]
                RECORD_STATUS = item["RECORD_STATUS"]
                PUNISH_DEADLINE = item["PUNISH_DEADLINE"]
                DATA_SOURCE_TYPE = item["DATA_SOURCE_TYPE"]
                STATE = item["STATE"]
                CREATE_TIME = item["CREATE_TIME"]
                CREATE_USER_ID = item["CREATE_USER_ID"]
                UPDATE_TIM = item["UPDATE_TIM"]
                UPDATE_USER_ID = item["UPDATE_USER_ID"]
                DELETE_TIME = item["DELETE_TIME"]
                DELETE_USER_ID = item["DELETE_USER_ID"]
                SECRET_DESCRIPTION = item["SECRET_DESCRIPTION"]
                IS_CAL = item["IS_CAL"]
                FRONT_TABLE_NAME = item["FRONT_TABLE_NAME"]

                exist = dbo_cdb.select_all(
                    f'select * from original_zfw_credit_record where ID="{ID}"'
                )
                if not exist:
                    params = {
                        "ID": ID,
                        "DATE_A": DATE_A,
                        "DEPARTMENT_ID": DEPARTMENT_ID,
                        "CREDIT_CODE": CREDIT_CODE,
                        "FIRST_ITEM_ID": FIRST_ITEM_ID,
                        "SECOND_ITEM_ID": SECOND_ITEM_ID,
                        "CREDIT_RECORD_TYPE": CREDIT_RECORD_TYPE,
                        "NOW_SCORE": NOW_SCORE,
                        "ORIGINAL_SCORE": ORIGINAL_SCORE,
                        "NOW_TOTAL_SCORE": NOW_TOTAL_SCORE,
                        "ORIGINAL_TOTAL_SCORE": ORIGINAL_TOTAL_SCORE,
                        "RETURN_SCORE": RETURN_SCORE,
                        "SCORE_TYPE": SCORE_TYPE,
                        "RECORD_STATUS": RECORD_STATUS,
                        "PUNISH_DEADLINE": PUNISH_DEADLINE,
                        "DATA_SOURCE_TYPE": DATA_SOURCE_TYPE,
                        "STATE": STATE,
                        "CREATE_TIME": CREATE_TIME,
                        "CREATE_USER_ID": CREATE_USER_ID,
                        "UPDATE_TIM": UPDATE_TIM,
                        "UPDATE_USER_ID": UPDATE_USER_ID,
                        "DELETE_TIME": DELETE_TIME,
                        "DELETE_USER_ID": DELETE_USER_ID,
                        "SECRET_DESCRIPTION": SECRET_DESCRIPTION,
                        "IS_CAL": IS_CAL,
                        "FRONT_TABLE_NAME": FRONT_TABLE_NAME,
                        "status": "1",
                        "reguser": "zhw",
                        "regtime": int(time.time()),
                    }
                    dbo_cdb.insert("original_zfw_credit_record", params)
                    print(f"添加信用记录{ID}")
                else:
                    params = {
                        "ID": ID,
                        "DATE_A": DATE_A,
                        "DEPARTMENT_ID": DEPARTMENT_ID,
                        "CREDIT_CODE": CREDIT_CODE,
                        "FIRST_ITEM_ID": FIRST_ITEM_ID,
                        "SECOND_ITEM_ID": SECOND_ITEM_ID,
                        "CREDIT_RECORD_TYPE": CREDIT_RECORD_TYPE,
                        "NOW_SCORE": NOW_SCORE,
                        "ORIGINAL_SCORE": ORIGINAL_SCORE,
                        "NOW_TOTAL_SCORE": NOW_TOTAL_SCORE,
                        "ORIGINAL_TOTAL_SCORE": ORIGINAL_TOTAL_SCORE,
                        "RETURN_SCORE": RETURN_SCORE,
                        "SCORE_TYPE": SCORE_TYPE,
                        "RECORD_STATUS": RECORD_STATUS,
                        "PUNISH_DEADLINE": PUNISH_DEADLINE,
                        "DATA_SOURCE_TYPE": DATA_SOURCE_TYPE,
                        "STATE": STATE,
                        "CREATE_TIME": CREATE_TIME,
                        "CREATE_USER_ID": CREATE_USER_ID,
                        "UPDATE_TIM": UPDATE_TIM,
                        "UPDATE_USER_ID": UPDATE_USER_ID,
                        "DELETE_TIME": DELETE_TIME,
                        "DELETE_USER_ID": DELETE_USER_ID,
                        "SECRET_DESCRIPTION": SECRET_DESCRIPTION,
                        "IS_CAL": IS_CAL,
                        "FRONT_TABLE_NAME": FRONT_TABLE_NAME,
                    }
                    dbo_cdb.update("original_zfw_credit_record", params, f'ID="{ID}"')
                    print(f"更新信用记录{ID}")
                dbo_ydb.update(
                    "dcv3_sdata_dir_eplist", {"extmark": "1"}, f'uscc="{uscc}"'
                )

    def run(self):
        self.start_credit_record()


if __name__ == "__main__":
    Crawl = Crawl()
    Crawl.run()
