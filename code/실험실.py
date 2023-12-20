import glob
import numpy as np

train=np.load("train data/randomforest/train_array/train4.npy")
label=np.load("train data/randomforest/label_array/label4.npy")

trainfileL=glob.glob("train data/randomforest/train_array/*.npy")
labelfileL=glob.glob("train data/randomforest/label_array/*.npy")



labelA=[]
for labelfile in labelfileL:
    labelA+=list(np.load(labelfile))
labelA=np.array(labelA,dtype=int)

labelA=np.array(sum([list(np.load(lbfile)) for lbfile in labelfileL],[]),dtype=int)

#trainA=np.array(sum([],[]),dtype=int)

print(len(labelA))


trainA=[]
for trainfile in trainfileL:
    for t in np.load(trainfile):
        #trainA=np.concatenate(trainA,t)
        trainA.append(list(t))
trainA=np.array(trainA)

trainA=np.array([list(t)for t in np.load(trainfile)for trainfile in trainfileL])
trainA=np.array([list(t)for trainfile in trainfileL for t in np.load(trainfile)])

print(len(trainA))

print(trainA[:2])
