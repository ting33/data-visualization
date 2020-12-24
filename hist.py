#直方图 看频率
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#造数据
s=np.random.randn(1000)

# #matplotlib画图
plt.hist(s,bins=20)  #bins是箱子数量
plt.show()

#seaborn画图
sns.displot(s,kde=True)  #kde表示是否展示密度曲线
plt.show()