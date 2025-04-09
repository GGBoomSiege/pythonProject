import numpy as np
from sklearn.linear_model import LinearRegression
from decimal import Decimal, getcontext

# 设置高精度计算
getcontext().prec = 50

# 定义股指B的最大值和股指A的最大值数据
B_max_new = np.array(
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
        4543,
        4537,
        4530,
        4512,
        4512,
        4514,
    ],
    dtype=np.float64,
)

A_max_new = np.array(
    [
        0.617,
        0.619,
        0.625,
        0.627,
        0.625,
        0.622,
        0.623,
        0.622,
        0.623,
        0.624,
        0.623,
        0.623,
        0.625,
        0.627,
        0.628,
        0.630,
        0.632,
        0.635,
        0.636,
        0.637,
        0.634,
        0.632,
        0.630,
        0.631,
        0.630,
        0.631,
        0.631,
        0.630,
        0.627,
        0.627,
        0.627,
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
