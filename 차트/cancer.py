import pandas as pd
import seaborn as sns
import matplotlib as plt
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
print("cancer type : \n",type(cancer))
print()
print("cancer's keys : \n",cancer.keys())
# print(cancer.items())

X, y = load_breast_cancer(return_X_y=True)
print("X : \n", X[:10])
print()
print("y : \n", y[:10])

df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
# df['target'] = cancer.target
print(df.head())

# 요소가 많을 때는 이런 그래프를 그리면 안된다. --> 보통 히트맵 분석으로 수행함
# pairplot, joint plot 은 특성의 개수가 많을때는 사용 금지!!!
# sns.pairplot(df, hue='target')
# plt.show()

# correct_matrix=df.drop(columns="target").corr()
# sns.heatmap(correct_matrix)
# plt.show()

