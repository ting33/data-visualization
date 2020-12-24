#散点图  适合展示两个变量之间的关系
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#造数据
#Matplotlib 要求原始数据的输入类型为 Numpy 数组
N=1000
x=np.random.randn(N)
y=np.random.randn(N)

#用matplotlib画图
plt.scatter(x,y,marker='x')
plt.title("Title")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


#用seaborn画图
#Seaborn 要求原始数据的输入类型为 pandas 的 Dataframe 或 Numpy 数组
df=pd.DataFrame({'x':x,'y':y})
sns.jointplot(x="x",y="y",data=df,kind='scatter')
plt.show()