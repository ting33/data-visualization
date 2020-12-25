#热力图是一种非常直观的多元变量分析方法
import seaborn as sns
import matplotlib.pyplot as plt
flights=sns.load_dataset("flights")
# print(flights.head())
data=flights.pivot(index='year',columns='month',values='passengers') #数据重塑
# print(data.head())
sns.heatmap(data)
plt.show()
