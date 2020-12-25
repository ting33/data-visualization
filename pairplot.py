#探索数据集中的多个成对双变量的分布
import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset('iris')
# print(iris.head())
sns.pairplot(iris)
plt.show()
