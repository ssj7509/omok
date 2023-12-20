import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 랜덤 숫자 행렬 생성
def generate_random_matrices(num_matrices, size):
    return [np.random.rand(size, size) for _ in range(num_matrices)]

# LTR 모델 학습
def train_ltr_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

# 우선순위 추출
def predict_priority(model, X_test):
    return model.predict(X_test)

# 행렬 생성
num_train_matrices = 100
num_test_matrices = 50
size = 100

train_matrices = generate_random_matrices(num_train_matrices, size)
test_matrices = train_matrices[20:50]

# 우선순위 설정 (여기서는 단순히 인덱스를 우선순위로 설정)
train_priorities = np.arange(num_train_matrices)
print(train_priorities)

# 행렬을 1차원으로 변환
X_train = np.array([m.flatten() for m in train_matrices])
X_test = np.array([m.flatten() for m in test_matrices])

# 모델 학습
model = train_ltr_model(X_train, train_priorities)

# 테스트 데이터에 대한 우선순위 예측
test_priorities = predict_priority(model, X_test)

# 결과 출력
print("Test priorities:", test_priorities)

