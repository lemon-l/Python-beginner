import matplotlib.pyplot as plt

# 设置饼图的数据，两个数据分布为1.然后展示是将所有数据填充同一个颜色即可。
slice = [1, 1]
plt.pie(slice, colors=['b', 'b'], explode=(0, 0))

# 显示椭圆公式
fig = plt.figure()
ax = fig.add_subplot(111)
ax.text(-0.75, -0.05, r'$ \frac{x^2}{a^2} + \frac{y^2}{b^2} =1 (a>b>0) $', fontsize=22)

plt.show()