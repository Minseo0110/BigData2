import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 성별에 따른 생존율 계산
titanic = sns.load_dataset('titanic')
# print(titanic['sex'].head())
# print(titanic.info())

# gender_survival = titanic.groupby(by='sex')['survived'].mean().reset_index()
# print(type(gender_survival))  # <class 'pandas.core.series.Series'>


gender_survival = titanic.groupby(by='sex')['survived'].mean().reset_index()
print(gender_survival)
# print(type(gender_survival))
print(gender_survival.info())

sns.barplot(data=gender_survival, x='sex', y='survived')
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.show()

# 생존자 수와 사망자 수 시각화
# sns.countplot(data=titanic, x='survived')
# plt.title('Survived (0 = No, 1 = Yes)')
# plt.xlabel('Survived')
# plt.ylabel('Count')
# plt.show()