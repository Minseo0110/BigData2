import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 나이에 따른 생존율 계산
titanic = sns.load_dataset('titanic')
# print(titanic.info())  # age 컬럼은 177개의 결측값이 존재

# 1) 결측치 행 제거
titanic_drop_row = titanic.dropna(subset=['age'])
#print(titanic_drop_row.info())
# 2) 생존율 계산
titanic_drop_row['survived'] = titanic_drop_row['survived'].astype(float)
print(titanic_drop_row['survived'])
# 3) 시각화
plt.figure(figsize=(10, 5))
sns.histplot(data=titanic_drop_row, x='age', weights='survived', bins=8, kde=True)
plt.title('Survival Rate by Age (Drop NaN rows)')
plt.xlabel('Age')
plt.ylabel('Survival Rate (Weighted)')
plt.show()


# print(titanic['sex'].head())
# print(titanic.info())

# gender_survival = titanic.groupby(by='sex')['survived'].mean().reset_index()
# print(type(gender_survival))  # <class 'pandas.core.series.Series'>

# gender_survival = titanic.groupby(by='sex')['survived'].mean().reset_index()
# print(gender_survival)
# # print(type(gender_survival))
# print(gender_survival.info())
#
# sns.barplot(data=gender_survival, x='sex', y='survived')
# plt.title('Survival Rate by Gender')
# plt.ylabel('Survival Rate')
# plt.show()

# 생존자 수와 사망자 수 시각화
# sns.countplot(data=titanic, x='survived')
# plt.title('Survived (0 = No, 1 = Yes)')
# plt.xlabel('Survived')
# plt.ylabel('Count')
# plt.show()