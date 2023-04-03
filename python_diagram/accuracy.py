import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimSun']  # 添加这条可以让图形显示中文
# plt.figure(figsize=(6, 4), dpi=300)
# x =  [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
x =  [0,5,10,15,20,25,30,35,45,55,65,75,85,95,110,125,130,145,160,180,200]
y1 = [0,25,35,43,50,56,62,67,73,79,82,86,87,88,88.6,88.6,88.6,88.6,88.6,88.6,88.6]
y2 = [0,15,24,33,41,48,54,60,66,71,76,81,84,86,87.9,87.9,87.9,87.9,87.9,87.9,87.9]
y3 = [0,20,38,50,59,67,74,76,78,79,80,81,82,83,84,85,85,85.4,85.4,85.4,85.4]
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

plt.plot(x, y1, 's-', color='#99CCFF', alpha=1, linewidth=1, label='CIFAR-10')
plt.plot(x, y2, '<-', color='#FF5722', alpha=1, linewidth=1, label='Heritage')
plt.plot(x, y3, 'o-', color='#FFC107', alpha=1, linewidth=1, label='Intel_image')

plt.legend(loc="lower right", fontsize=13)
plt.xlabel('训练轮次', fontsize = 14)
plt.ylabel('准确率%', fontsize = 14)
plt.tick_params(labelsize=14)  #刻度字体大小13
plt.show()