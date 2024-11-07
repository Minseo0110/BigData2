import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
#titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
#titanic['deck'].fillna('Unknown', inplace=True)
#print(titanic['deck'])
#print(titanic.info())

#print(titanic['survived'])
#print(titanic.info())

# 생존자 수와 사망자 수 시각화
sns.countplot(data=titanic, x='survived')
plt.title('Survived (0 = No, 1 = Yes)')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()