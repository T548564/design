import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimSun']  # 添加这条可以让图形显示中文
# plt.figure(figsize=(10, 10), dpi=300)

df1 = pd.read_csv('./csv/Intel_images/3_4/Intel_images_3_4_64_source.csv')
df2 = pd.read_csv('./csv/Intel_images/3_4/Intel_images_3_4_64_fineTune.csv')
df3 = pd.read_csv('./csv/Intel_images/3_4/Intel_images_3_4_64_prune_0.1.csv')
df4 = pd.read_csv('./csv/Intel_images/3_4/Intel_images_3_4_64_prune_0.3.csv')
df5 = pd.read_csv('./csv/Intel_images/3_4/Intel_images_3_4_64_prune_0.5.csv')


df6 = pd.read_csv('./csv/heritage/3_0/Heritage_3_0_512_distillation.csv')  # distillation
df7 = pd.read_csv('./csv/cifar10/4_2/cifar10_4_2_512_distillation.csv')  # irrelevant
y1 = list(df1['distance(3->4)'])
y2 = list(df2['distance(3->4)'])
y3 = list(df3['distance(3->4)'])
y4 = list(df4['distance(3->4)'])
y5 = list(df5['distance(3->4)'])
y6 = list(df6['distance(3->0)'])
y7 = list(df7['distance(4->2)'])
# print(max(y))
x = [i for i in range(1, 65, 3)]
y1 = y1[:: 3]
y2 = y2[:: 3]
y3 = y3[:: 3]
y4 = y4[:: 3]
y5 = y5[:: 3]
y6 = y6[384: 448: 3]
y7 = y7[384: 448: 3]
plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内`
plt.xlim(-2, 67)
plt.ylim(-0.05, 1)
x_major_locator=MultipleLocator(10)#以每15显示
y_major_locator=MultipleLocator(0.2)#以每3显示
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.plot(x, y1, 's-', color='#1A237E', alpha=1, linewidth=1, label='源模型')
plt.plot(x, y2, '+-', color='#FF5722', alpha=1, linewidth=1, label='微调')
plt.plot(x, y3, 'o-', color='#E53935', alpha=1, linewidth=1, label='剪枝10%')
plt.plot(x, y4, '^-', color='#43A047', alpha=1, linewidth=1, label='剪枝30%')
plt.plot(x, y5, 'v-', color='#FFC107', alpha=1, linewidth=1, label='剪枝50%')
plt.plot(x, y6, '*-', color='#424242', alpha=1, linewidth=1, label='知识蒸馏')
plt.plot(x, y7, 'x-', color='#9575CD', alpha=1, linewidth=1, label='无关模型')
# 显示标签，如果不加这句，即使在plot中加了label='一些数字'的参数，最终还是不会显示标签
plt.legend(loc="upper left", fontsize=16)
plt.xlabel('近边界数据数量', fontsize = 24)
plt.ylabel('距离分类边界距离', fontsize = 24)
plt.tick_params(labelsize=20)  #刻度字体大小13
# plt.savefig('../yzw/image/Intel_image-3-4-distance.png', dpi = 600)
plt.show()