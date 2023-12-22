import numpy as np
import analyzer_v2 as anl

def converter(s):
    return [(x,int(y))for x,y in zip((ord(c)-96 for c in s if c.isalpha()),''.join((c,' ')[c.isalpha()]for c in s).split())]

with open("train data/slow_game_1.txt","r") as f:
    gameL=[converter(s)for s in f.read().split('\n')]

with open("train data/index_Label.txt","a") as f:
    count=1
    for game in gameL:
        for i in range(1,len(game)-1):
            x,y=game[i+1]
            x,y=x-1,y-1
            xyL,arrayT=anl.main_play(game[:i],1)
            if (x,y) not in xyL:
                continue
            index=xyL.index((x,y))

            np.save(f"train data/numpy_data4/data{count}.npy",np.array(arrayT))
            f.write(f"{index}\n")

            count+=1

            

