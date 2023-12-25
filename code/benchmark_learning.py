import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def vector_matrix_mult(vector, matrix):
    result = np.zeros(matrix.shape[1])
    for i in range(matrix.shape[1]):
        for j in range(vector.shape[0]):
            result[i] += vector[j] * matrix[j][i]
    return result

def feed_forward(game, w1, w2, w3):
    y1 = sigmoid(vector_matrix_mult(game, w1))
    y2 = sigmoid(vector_matrix_mult(y1, w2))
    y3 = sigmoid(vector_matrix_mult(y2, w3))

    return y1, y2, y3

def get_w(fname):
    w1=np.load(f"weights/{fname}_w1.npy")
    w2=np.load(f"weights/{fname}_w2.npy")
    w3=np.load(f"weights/{fname}_w3.npy")

    return w1,w2,w3

def get_xy(indexT,gameT,fname):
    w1,w2,w3=get_w(fname)
    xy=predict(indexT,gameT,w1,w2,w3)

    return xy

def predict(indexT,gameT,w1,w2,w3):
    y3A=np.empty(0)
    for g in range(len(gameT)):
        y1,y2,y3=feed_forward(gameT[g],w1,w2,w3)
        y3A=np.concatenate((y3A,y3))

    maxv=np.max(y3A)

    return [indexT[i] for i,n in enumerate(y3A) if n==maxv]
