import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

mpg = sns.load_dataset('mpg')  # 데이터 셋 로딩

# 데이터 전처리
mpg.drop(['name'], axis=1, inplace=True)  # 불필요한 컬럼 삭제
mpg.dropna(inplace=True)  # 결측치가 있는 행 제거 (원본 데이터 변경)
mpg = pd.get_dummies(mpg, columns=['origin'], drop_first=True)  # One-hot encoding
# print(mpg.info())

# 독립변수, 의존변수
X = mpg.drop(['mpg'], axis=1)  # 레이블 컬럼 제거
y = mpg['mpg']  # 레이블 (타겟 변수)
# print(X.dtypes)  # 각 열의 데이터 타입 확인