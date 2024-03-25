from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터 로드
iris = load_iris()
X, y = iris.data, iris.target

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 인공 신경망 모델 생성
model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)

# 모델 학습
model.fit(X_train, y_train)

# 모델 예측
y_pred = model.predict(X_test)
print(y_pred)

# 모델 성능 평가
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)