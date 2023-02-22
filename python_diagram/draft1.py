import matplotlib.pyplot as plt
import numpy as np
# 设定画布。dpi越大图越清晰，绘图时间越久
# fig=plt.figure(figsize=(6, 6), dpi=300)


import pandas as pd

# df = pd.read_csv('./csv/cifar10/4_2/cifar10_4_2_64_source.csv')
# # print(df['distance(4->2)'])
# a = list(df['distance(4->2)'])
# print(a)
# x = [i for i in range(1, 65, 3)]
# print(x)
#
# y = x[: : -1]
# print(y)

df6 = pd.read_csv('./csv/heritage/3_0/Heritage_3_0_512_distillation.csv')

y = list(df6['distance(3->0)'])
print(len(y))

x1 = y[0: 64: 3]
print(len(x1))

x2 = y[64: 128: 3]
print(len(x2))

x3 = y[128: 192: 3]
print(len(x3))