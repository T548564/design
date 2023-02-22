import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文
# plt.figure(figsize=(6, 4), dpi=300)
x = [64, 128, 256, 512, 1024]
y1 = [-4, -6, -6, -8, -8]
y2 = [-2, -4, -4, -6, -6]
y3 = [-3, -4, -5, -7, -8]
y4 = [-3, -4, -5, -5, -6]
y5 = [-3, -3, -4, -4, -6]
y6 = [-2, -4, -4, -5, -6]

plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内`
plt.xlim(-50, 1100)
plt.ylim(-8.4, -1.5)
x_major_locator = MultipleLocator(200)  # 以每15显示
y_major_locator = MultipleLocator(1)  # 以每3显示
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

plt.plot(x, y1, 's-', color='#1A237E', alpha=1, linewidth=1, label='源模型')
plt.plot(x, y2, 'o-', color='#E53935', alpha=1, linewidth=1, label='剪枝10%')
plt.plot(x, y3, '^-', color='#43A047', alpha=1, linewidth=1, label='剪枝30%')
plt.plot(x, y4, 'v-', color='#FFC107', alpha=1, linewidth=1, label='剪枝50%')
plt.plot(x, y5, '<-', color='#FF5722', alpha=1, linewidth=1, label='微调')
plt.plot(x, y6, 'x-', color='tan', alpha=1, linewidth=1, label='知识蒸馏')

plt.legend(loc="upper right")
plt.xlabel('近边界数据数量')
plt.ylabel('log(p值)')
plt.savefig('./pic/Intel_image-3-4-p-value.png', dpi=300)
plt.show()