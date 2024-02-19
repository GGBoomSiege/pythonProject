# api host和端口
API_HOST = "0.0.0.0"
API_PORT = 6066


# MySQL配置
MYSQL_CHOST = "117.149.210.103"
MYSQL_CPORT = 3306
MYSQL_CUSER = "builtin"
MYSQL_CPASSWD = "builtin@Lhwx123456"
MYSQL_CDB = "zjwzw_dc_original"



# 新增入库苗圃企业：新增入库苗圃“重点企业”苏州****有限公司
# 在库企业升级：苏州****有限公司从“基础企业”升级为“重点企业”
# 在库企业出库：苏州****有限公司注销，自动调整出库
# 新获得服务券：苏州****有限公司新获得苗圃企业服务券
# 服务券到期：苏州****有限公司苗圃企业服务券到期
# 购买服务产品：苏州****有限公司购买服务产品“苗圃线上商学院”

# 苗圃企业层级
NURSERY_LEVEL = {
    "基础企业":"10",
    "重点企业":"11",
    "拟上市企业":"12",
    "上市企业":"13",
}

NURSERY_LEVEL_01 = "10"
NURSERY_LEVEL_02 = "11"
NURSERY_LEVEL_03 = "12"
NURSERY_LEVEL_04 = "13"

OUT_LEVEL_IN = "10"  # 在库
OUT_LEVEL_OUT = "20"  # 出库

# 出库原因
OUT_REASON_01 = "企业迁出"
OUT_REASON_02 = "企业上市"
OUT_REASON_03 = "企业注销"
OUT_REASON_04 = "企业吊销"

# 苗圃感知类型
PERCEPTION_TYPE_01 = "新增入库苗圃企业"
PERCEPTION_TYPE_02 = "在库企业升级"
PERCEPTION_TYPE_03 = "在库企业出库"
PERCEPTION_TYPE_04 = "新获得服务券"
PERCEPTION_TYPE_05 = "购买服务产品"

# 入库状态
OUT_LEVEL = {
    "在库":"10",
    "出库":"20",
}

# 有效状态
STATUS_LEVEL = {
    "有效":"10",
    "失效":"20",
}

voucherstatus_dict = {"effective":"有效",  "":"已过期"}

applystatus_dict = {
    "approvePass":"审核通过",
    "pendingSubmit":"待提交",
    "pendingApproveLevel":"待审核",
    "approveReturn":"已退回"}
