import numpy as np
from sklearn.linear_model import LinearRegression
from decimal import Decimal, getcontext

# 设置高精度计算
getcontext().prec = 50

# 定义股指B的最大值和股指A的最大值数据
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

# 截取 B_max_new 的前 31 个数据点，确保长度一致
B_max_new = B_max_new[:31]

# 使用高精度的 B_max 和 A_max 数据进行回归
B_max_decimal = np.array([Decimal(x) for x in B_max_new])
A_max_decimal = np.array([Decimal(x) for x in A_max_new])

# 构造特征矩阵，包括B_max和B_max^2
X_decimal = np.column_stack((B_max_decimal**2, B_max_decimal))

# 创建线性回归模型
model_decimal = LinearRegression()

# 训练模型，使用B_max^2和B_max作为输入特征，A_max作为目标值
model_decimal.fit(X_decimal, A_max_decimal)

# 获取回归系数和截距
alpha_decimal = Decimal(model_decimal.coef_[0])
beta_decimal = Decimal(model_decimal.coef_[1])
gamma_decimal = Decimal(model_decimal.intercept_)

# 输出最终的二次回归公式
print(
    f"回归公式：A_max = ({alpha_decimal}) * B_max^2 + ({beta_decimal}) * B_max + ({gamma_decimal})"
)
