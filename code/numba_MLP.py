from numba import njit
import numpy as np
import glob

@njit
def sigmoid(x):
    return 1/(1+np.exp(-x))

@njit
def derivative_sigmoid(x):
    return x*(1-x)

@njit
def vector_matrix_mult(vector, matrix):
    result = np.zeros(matrix.shape[1])
    for i in range(matrix.shape[1]):
        for j in range(vector.shape[0]):
            result[i] += vector[j] * matrix[j][i]
    return result

@njit
def feed_forward(game, w1, w2, w3):
    y1 = sigmoid(vector_matrix_mult(game, w1))
    y2 = sigmoid(vector_matrix_mult(y1, w2))
    y3 = sigmoid(vector_matrix_mult(y2, w3))

    return y1, y2, y3

@njit
def back_propagation(game, y1, y2, y3, t, w1, w2, w3, lrate, max_index):
    d3 = np.zeros(1)
    d3[0] = (t - y3) * derivative_sigmoid(y3)

    d2 = vector_matrix_mult(d3, np.transpose(w3)) * derivative_sigmoid(y2)
    d1 = vector_matrix_mult(d2, np.transpose(w2)) * derivative_sigmoid(y1)

    w3 += lrate * np.outer(y2, d3)
    w2 += lrate * np.outer(y1, d2)
    w1 += lrate * np.outer(game, d1)

    return w1, w2, w3
'''
@njit
def train(gameT,indexT,inner_epoch,outer_epoch,w1,w2,w3,lrate):
    for outer in range(outer_epoch):
        print(outer)
        for i in range(len(gameT)):
            game=gameT[i]
            max_index=indexT[i]

            for inner in range(inner_epoch):
                y1A=np.empty(0)
                y2A=np.empty(0)
                y3A=np.empty(0)
                
                for g in range(len(game)):
                    y1,y2,y3=feed_forward(game[g],w1,w2,w3)
                    y1A=np.concatenate((y1A,y1))
                    y2A=np.concatenate((y2A,y2))
                    y3A=np.concatenate((y3A,y3))
                
                if inner%1000==0:
                    #print(np.argmax(y3A),max_index)
                    print(f"\tinner {100*(inner+1000)//inner_epoch}%")
                
                if np.argmax(y3A)==max_index:
                    print("check")
                    print(len(y3A),len(game))
                    break

                for g in range(len(game)):
                    if g!=max_index:
                        #t=y3A[g]*0.8
                        t=0
                    else:
                        #t=y3A[g]*1.2
                        t=1
                    w1,w2,w3=back_propagation(game[g],y1A[g],y2A[g],y3A[g],t,w1,w2,w3,lrate,max_index)
            print(f"outer {outer} : game {i} clear")
        #print(f"outer {100*(outer+1)//outer_epoch}%")                
    return w1,w2,w3
'''

@njit
def train(gameT,indexT,inner_epoch,outer_epoch,w1,w2,w3,lrate):
    for outer in range(outer_epoch):
        print(outer)
        cnt2=0
        for i in range(len(gameT)):
            game=gameT[i]
            max_index=indexT[i]

            cnt=0
            #print(max_index)
            while True:
                y1A=np.empty(0)
                y2A=np.empty(0)
                y3A=np.empty(0)

                
                #lrate=0.01*(1+1*cnt2//10000)
                for g in range(len(game)):
                    y1,y2,y3=feed_forward(game[g],w1,w2,w3)
                    y1A=np.concatenate((y1A,y1))
                    y2A=np.concatenate((y2A,y2))
                    y3A=np.concatenate((y3A,y3))
                '''
                if cnt%10000==0:
                    #print(np.argmax(y3A),max_index)
                    print(f"cnt : {cnt}")
                    print(np.max(y3A)-y3A[max_index])
                    print(y3A)
                '''
                if y3A[max_index]==np.max(y3A):
                    print("check")
                    print(game[0][0])
                    print(np.max(y3A)-y3A[max_index])
                    break

                if (cnt+1)%10==0:
                    print(np.max(y3A)-y3A[max_index])
                    break

                for g in range(len(game)):
                    if y3A[max_index]==np.max(y3A):
                        print("check2")
                        print(game[0][0])
                        print(np.max(y3A)-y3A[max_index])
                        break
                    if g!=max_index and y3A[g]>y3A[max_index]:
                        #t=y3A[g]*0.5
                        t=0
                    elif g==max_index or y3A[g]==y3A[max_index]:
                        #t=y3A[g]*1.5
                        t=10
                    else:
                        continue
                    w1,w2,w3=back_propagation(game[g],y1A[g],y2A[g],y3A[g],t,w1,w2,w3,lrate,max_index)
                cnt+=1
                cnt2+=1
            print(f"outer {outer} : game {i} clear")
        #print(f"outer {100*(outer+1)//outer_epoch}%")                
    return w1,w2,w3


def test(gameT,indexT,w1,w2,w3):
    for i in range(10):
        gameT[i]
        indexT[i]

        
with open("train data/index_Label.txt","r") as f:
    indexT=tuple(map(int,f.read().split()))

fileL=glob.glob("train data/numpy_data4/*.npy")
gameT=tuple(np.load(file)for file in fileL)

DIM=(36,15,7,1)


w1=np.random.rand(DIM[0],DIM[1])
w2=np.random.rand(DIM[1],DIM[2])
w3=np.random.rand(DIM[2],DIM[3])
print(len(w1),len(w2),len(w3))

'''
w1=np.random.randn(DIM[0],DIM[1])*np.sqrt(2.0/DIM[0])
w2=np.random.randn(DIM[1],DIM[2])*np.sqrt(2.0/DIM[2])
w3=np.random.randn(DIM[2],DIM[3])*np.sqrt(2.0/DIM[3])
print(len(w1),len(w2),len(w3))
'''
lrate=0.1

inner_epoch=10000
outer_epoch=10
#print(indexT)
#test(gameT,indexT,w1,w2,w3)
w1,w2,w3=train(gameT,indexT,inner_epoch,outer_epoch,w1,w2,w3,lrate)
print(w1)
print(w2)
print(w3)

np.save("weights/14_w1.npy",w1)
np.save("weights/14_w2.npy",w2)
np.save("weights/14_w3.npy",w3)
