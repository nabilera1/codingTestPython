from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 인위적인 데이터셋 만들기, n개의 무작위 데이터 클러스트링 생성
X, y=make_blobs(random_state=0)
# 데이터와 타깃 레이블을 훈련 셋과 테스트 셋으로 나눈다.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# 모델 객체를 만들고 훈련 셋으로 학습시킨다.
logreg=LogisticRegression().fit(X_train, y_train)
# 모델을 테스트 셋으로 평가한다.
print("테스트 셋 점수 :{:.2f}".format(logreg.score(X_test,y_test)))
# 테스트 셋 점수 :0.88
# 데이터셋, train test split, fit, model생성, model score(테스트 데이터셋)
# 데이터를 훈련셋과 테스트셋으로 나누는 이유는
# 앞으로 테스트해 볼 새로운 데이터셋에 현재 만들어진 모델이
# 얼마나 잘 일반화되어 있는지 측정하기 위해서이다.
#
