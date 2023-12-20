import glob,joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier


# LTR 모델 학습
def train_ltr_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, max_depth=15, min_samples_split=5)
    model.fit(X_train, y_train)
    return model

trainfileL=glob.glob("train data/randomforest/train_array/*.npy")
labelfileL=glob.glob("train data/randomforest/label_array/*.npy")

labelA=np.array(sum([list(np.load(lbfile)) for lbfile in labelfileL],[]),dtype=int)
trainA=np.array([list(t)for trainfile in trainfileL for t in np.load(trainfile)])

# 모델 학습
model = train_ltr_model(trainA,labelA)
joblib.dump(model,"randomforest_model/model1.joblib")


