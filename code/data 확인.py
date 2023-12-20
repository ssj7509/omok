import numpy as np
import glob

def f(stance,prior_val,shape):
    return 1+stance*10+(prior_val-1)*(2,5)[stance]+shape

fileL=glob.glob("train data/numpy_data4/*.npy")
s=np.zeros(36)


for file in fileL:
    for array in np.load(file):
        #print(array)
        s+=array

print(s.astype('int'))


L=[0]*36
a=np.zeros(36)

for stance in range(2):
    for prior_val in range(1,6):
        for shape in (range(2),range(5))[stance]:
            a[f(stance,prior_val,shape)]+=1
            
            if s[f(stance,prior_val,shape)]==0:
                print(stance,prior_val,shape)
            


print(a)


print(f(0,4,0))
