#折线图可以用来表示数据随着时间变化的趋势。
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#造数据
N=1000
x=np.random.randn(N)
y=np.random.randn(N)
#x需要从小到大排序，这样才有利于观察
x.sort()

#用matplotlib画图
plt.plot(x,y)
plt.show

#用seaborn
df=pd.DataFrame({'x':x,'y':y})
sns.lineplot(x="x",y="y",data=df)
plt.show()