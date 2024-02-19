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

    def start_enterprise_credit(self):
        token = self.gettoken()
        print(token)
        Authorization = "jwt " + token
        self.header["Authorization"] = Authorization
        print(self.header)
        uscc_list = dbo_ydb.select_all(
            "select * from dcv3_sdata_dir_eplist where notes is null"
        )
        for item in uscc_list:
            uscc = item["uscc"]
            if not uscc:
                continue
            self.payload["p_credit_code"] = uscc
            response = requests.post(
                url=self.url_3, headers=self.header, json=self.payload
            )
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
                        url=self.url_3, headers=self.header, json=self.payload
                    )
            josn_items = json.loads(response.text)["datas"]

            if not josn_items:
                continue

            for item in josn_items:
                ID = item["ID"]
                ENTERPRISE_NAME = item["ENTERPRISE_NAME"]
                CREDIT_CODE = item["CREDIT_CODE"]
                REPRESENTER = item["REPRESENTER"]
                PHONE = item["PHONE"]
                ADDRESS = item["ADDRESS"]
                LONGITUDE = item["LONGITUDE"]
                LATITUDE = item["LATITUDE"]
                ENTERPRISE_TYPE = item["ENTERPRISE_TYPE"]
                INDUSTRY_TYPE = item["INDUSTRY_TYPE"]
                REGISTER_DATE = item["REGISTER_DATE"]
                ADM_DIVISION = item["ADM_DIVISION"]
                ENTERPRISE_LABEL = item["ENTERPRISE_LABEL"]
                SAFE_GRID = item["SAFE_GRID"]
                CREDIT_SCORE = item["CREDIT_SCORE"]
                CREDIT_LEVEL = item["CREDIT_LEVEL"]
                CREDIT_STATUS = item["CREDIT_STATUS"]
                DISTRICT_CREDIT_SCORE = item["DISTRICT_CREDIT_SCORE"]
                STATE = item["STATE"]
                CREATE_TIME = item["CREATE_TIME"]
                CREATE_USER_ID = item["CREATE_USER_ID"]
                UPDATE_TIME = item["UPDATE_TIME"]
                UPDATE_USER_ID = item["UPDATE_USER_ID"]
                MANAGE_SCOPE = item["MANAGE_SCOPE"]

                exist = dbo_cdb.select_all(
                    f'select * from original_zfw_enterprise_credit where ID="{ID}"'
                )
                if not exist:
                    params = {
                        "ID": ID,
                        "ENTERPRISE_NAME": ENTERPRISE_NAME,
                        "CREDIT_CODE": CREDIT_CODE,
                        "REPRESENTER": REPRESENTER,
                        "PHONE": PHONE,
                        "ADDRESS": ADDRESS,
                        "LONGITUDE": LONGITUDE,
                        "LATITUDE": LATITUDE,
                        "ENTERPRISE_TYPE": ENTERPRISE_TYPE,
                        "INDUSTRY_TYPE": INDUSTRY_TYPE,
                        "REGISTER_DATE": REGISTER_DATE,
                        "ADM_DIVISION": ADM_DIVISION,
                        "ENTERPRISE_LABEL": ENTERPRISE_LABEL,
                        "SAFE_GRID": SAFE_GRID,
                        "CREDIT_SCORE": CREDIT_SCORE,
                        "CREDIT_LEVEL": CREDIT_LEVEL,
                        "CREDIT_STATUS": CREDIT_STATUS,
                        "DISTRICT_CREDIT_SCORE": DISTRICT_CREDIT_SCORE,
                        "STATE": STATE,
                        "CREATE_TIME": CREATE_TIME,
                        "CREATE_USER_ID": CREATE_USER_ID,
                        "UPDATE_TIME": UPDATE_TIME,
                        "UPDATE_USER_ID": UPDATE_USER_ID,
                        "MANAGE_SCOPE": MANAGE_SCOPE,
                        "status": "1",
                        "reguser": "zhw",
                        "regtime": int(time.time()),
                    }
                    dbo_cdb.insert("original_zfw_enterprise_credit", params)
                    print(f"添加企业信用{ENTERPRISE_NAME}")
                else:
                    params = {
                        "ID": ID,
                        "ENTERPRISE_NAME": ENTERPRISE_NAME,
                        "CREDIT_CODE": CREDIT_CODE,
                        "REPRESENTER": REPRESENTER,
                        "PHONE": PHONE,
                        "ADDRESS": ADDRESS,
                        "LONGITUDE": LONGITUDE,
                        "LATITUDE": LATITUDE,
                        "ENTERPRISE_TYPE": ENTERPRISE_TYPE,
                        "INDUSTRY_TYPE": INDUSTRY_TYPE,
                        "REGISTER_DATE": REGISTER_DATE,
                        "ADM_DIVISION": ADM_DIVISION,
                        "ENTERPRISE_LABEL": ENTERPRISE_LABEL,
                        "SAFE_GRID": SAFE_GRID,
                        "CREDIT_SCORE": CREDIT_SCORE,
                        "CREDIT_LEVEL": CREDIT_LEVEL,
                        "CREDIT_STATUS": CREDIT_STATUS,
                        "DISTRICT_CREDIT_SCORE": DISTRICT_CREDIT_SCORE,
                        "STATE": STATE,
                        "CREATE_TIME": CREATE_TIME,
                        "CREATE_USER_ID": CREATE_USER_ID,
                        "UPDATE_TIME": UPDATE_TIME,
                        "UPDATE_USER_ID": UPDATE_USER_ID,
                        "MANAGE_SCOPE": MANAGE_SCOPE,
                    }
                    dbo_cdb.update(
                        "original_zfw_enterprise_credit", params, f'ID="{ID}"'
                    )
                    print(f"更新企业信用{ENTERPRISE_NAME}")
                params = {"notes": "1"}
                dbo_ydb.update("dcv3_sdata_dir_eplist", params, f'uscc="{uscc}"')

    def run(self):
        self.start_enterprise_credit()


if __name__ == "__main__":
    Crawl = Crawl()
    Crawl.run()
