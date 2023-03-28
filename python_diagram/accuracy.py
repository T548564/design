import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文
# plt.figure(figsize=(6, 4), dpi=300)
x =  [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
y1 = [0,35,40,42,46,50,60,70,75,80,85,86,87,88,88.6,88.6,88.6,88.6,88.6,88.6,88.6]
# y2 = [i for i in range(3,70)]
# y3 = [i for i in range(5,72)]


plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内`
plt.xlim(-5, 210)
plt.ylim(-5, 100)
x_major_locator = MultipleLocator(25)  # 以每15显示
y_major_locator = MultipleLocator(20)  # 以每3显示
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

plt.plot(x, y1, 'v-', color='#FFC107', alpha=1, linewidth=1, label='CIFAR-10')
# plt.plot(x, y2, '<-', color='#FF5722', alpha=1, linewidth=1, label='Heritage')
# plt.plot(x, y3, 'o-', color='#E53935', alpha=1, linewidth=1, label='Intel_image')

plt.legend(loc="lower right", fontsize=16)
plt.xlabel('训练轮次', fontsize = 20)
plt.ylabel('准确率%', fontsize = 20)
plt.tick_params(labelsize=16)  #刻度字体大小13
plt.show()