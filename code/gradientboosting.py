import glob,joblib
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier

trainfileL=glob.glob("train data/randomforest/train_array/*.npy")
labelfileL=glob.glob("train data/randomforest/label_array/*.npy")

labelA=np.array(sum([list(np.load(lbfile)) for lbfile in labelfileL],[]),dtype=int)
trainA=np.array([list(t)for trainfile in trainfileL for t in np.load(trainfile)])

model=GradientBoostingClassifier()
model.fit(trainA,labelA)

joblib.dump(model,"randomforest_model/model2.joblib")
