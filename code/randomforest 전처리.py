import numpy as np
import analyzer as anl

def converter(s):
    return [(x,int(y))for x,y in zip((ord(c)-96 for c in s if c.isalpha()),''.join((c,' ')[c.isalpha()]for c in s).split())]

with open("train data/slow_game_1.txt","r") as f:
    gameL=[converter(s)for s in f.read().split('\n')]

count=1
for game in gameL:
    for i in range(1,len(game)-1):
        x,y=game[i+1]
        x,y=x-1,y-1
        xyL,arrayT=anl.main_play(game[:i],1)
        
        if (x,y) not in xyL:
            continue
        ai_select=xyL.index((x,y))
        indexL=[index for index,array in enumerate(arrayT) if all(array==arrayT[ai_select])]
        
        max_abs=arrayT[0][0]*2
        priorA=np.zeros(len(xyL),dtype=int)+max_abs

        for index in indexL:
            priorA[index]+=1
        

        np.save(f"train data/randomforest/train_array/train{count}.npy",np.array(arrayT))
        np.save(f"train data/randomforest/label_array/label{count}.npy",np.array(priorA))

        count+=1
