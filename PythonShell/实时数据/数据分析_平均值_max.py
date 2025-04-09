import numpy as np
from sklearn.linear_model import LinearRegression
from decimal import Decimal, getcontext

# 设置高精度计算
getcontext().prec = 50

# 定义股指B的最大值和最小值数据
B_max_new = np.array(
    [
        4472,
        4518,
        4540,
        4550,
        4520,
        4511,
        4509,
        4503,
        4516,
        4517,
        4510,
        4513,
        4530,
        4533,
        4554,
        4564,
        4605,
        4601,
        4626,
        4619,
        4594,
        4569,
        4555,
        4552,
        4552,
        4552,
        4572,
        4569,
        4546,
        4533,
        4522,
        4528,
    ],
    dtype=np.float64,
)

B_min_new = np.array(
    [
        4446,
        4470,
        4504,
        4518,
        4507,
        4484,
        4490,
        4479,
        4495,
        4500,
        4490,
        4494,
        4503,
        4518,
        4531,
        4539,
        4560,
        4570,
        4595,
        4587,
        4561,
        4552,
        4540,
        4538,
        4536,
        4536,
        4543,
        4537,
        4530,
        4512,
        4512,
        4514,
    ],
    dtype=np.float64,
)

# 计算股指B的平均值（B_avg）
B_avg_new = (B_max_new + B_min_new) / 2

# 定义股指A的最大值数据（A_max）
A_max_new = np.array(
    [
        0.619,
        0.625,
        0.630,
        0.631,
        0.626,
        0.626,
        0.625,
        0.624,
        0.625,
        0.626,
        0.625,
        0.626,
        0.628,
        0.628,
        0.631,
        0.633,
        0.638,
        0.637,
        0.641,
        0.640,
        0.637,
        0.634,
        0.632,
        0.631,
        0.632,
        0.635,
        0.635,
        0.632,
        0.630,
        0.628,
        0.629,
    ],
    dtype=np.float64,
)

B_avg_new = B_avg_new[:31]

# 将数据转化为Decimal类型以保证高精度
B_avg_decimal = np.array([Decimal(x) for x in B_avg_new])
A_max_decimal = np.array([Decimal(x) for x in A_max_new])

# 构造特征矩阵，包括B_avg 和 B_avg^2
X_decimal = np.column_stack((B_avg_decimal, B_avg_decimal**2))

# 创建线性回归模型
model_decimal = LinearRegression()

# 训练模型，使用 B_avg 和 B_avg^2 作为输入特征，A_max 作为目标值
model_decimal.fit(X_decimal, A_max_decimal)

# 获取回归系数和截距
alpha_decimal = Decimal(model_decimal.coef_[0])
beta_decimal = Decimal(model_decimal.coef_[1])
intercept_decimal = Decimal(model_decimal.intercept_)

# 输出最终的回归公式
print(
    f"回归公式：A_max = ({alpha_decimal}) * B_avg + ({beta_decimal}) * B_avg^2 + ({intercept_decimal})"
)
