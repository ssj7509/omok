import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 우선순위 추출
def predict_priority(model, X_test):
    return model.predict(X_test)

def get_xy(indexT,gameT,fname):
    model=joblib.load(f"randomforest_model/model{fname}.joblib")
    x_Test=np.array([list(t)for t in gameT])
    predictL=predict_priority(model,x_Test)

    minN=min(predictL)
    print(predictL)
    
    return [indexT[i]for i,n in enumerate(predictL) if n==minN]
