import numpy as np
import eigen
import time

# mat = [[[2,0,1],[1,2,1],[0,2,4]],
# [[1,0,2],[0,1,1],[1,2,2]],
# [[1,2,3],[2,4,3],[1,2,3]]]
# print(mat)

def Flatten(m):
# mengubah himpunan face vector dgn size M x N x N menjadi M x N^2
    a = np.reshape(m,(len(m),len(m[0])*len(m[0])),order='F')

def Unflatten(m):
# mengubah himpunan face vector dgn size M x 256^2 menjadi M x N x N
    return np.reshape(m,(-1,256,256),order='F')


def Average(m):
# mengembalikan average dari face vector
    return np.mean(m, axis=0)

def Selisih(avg,m):
# mengurangi setiap face vector dengan average
    selisih = []
    for i in range(len(m)):
        selisih.append(np.subtract(m[i],avg))
    return selisih

def Covarian(selisih):
# mengembalikan matrix covarian (M x M)
    At = selisih # ukuran M x N^2
    Aa = np.transpose(selisih) # ukuran N^2 x M
    return np.divide(np.matmul(At,Aa),len(selisih))

def EigenvectorAtA(m):
# mengembalikan eigen vector dari matrix m
    (eigenvalue,eigenvector) = np.linalg.eig(m)

    # idx = eigenvalue.argsort()[::-1]
    # eigenvalue = eigenvalue[idx]
    # eigenvector=eigenvector[:,idx]

    return eigenvector

def EigenvectorAAt(eigenvectorAtA,selisih):
# mengengubah eigenvector At x A menjadi eigenvector A x At
    return np.transpose(np.matmul(np.transpose(selisih),np.transpose(eigenvectorAtA)))

def normalizeEigenVector(eigenvector):
# mengembalikan eigenvector yang telah di normalize
    normalize = []
    for i in range(len(eigenvector)):
        # normalize.append(eigenvector[i]/np.linalg.norm(eigenvector[i]))
        normalize.append(eigenvector[i]/eigen.magnitude(eigenvector[i]))
    return normalize

def Weight(eigenvector,selisih):
# mengembalikan bobot eigenvector setiap faces vector   
    weight = []
    temp = []
    for i in range(len(selisih)):
        temp = []
        for j in range(len(eigenvector)):
            temp.append(np.matmul(eigenvector[j],np.transpose(selisih[i])))
        weight.append(temp)
    return weight

def Reconstruct(avg,eigenvector,weight):
# mengembalikan img yang telah di rekonstruksi
    reconstruct = []
    for i in range(len(weight)):
        x = np.sum([avg,np.matmul(np.transpose(eigenvector),np.transpose(weight[i]))],axis=0)
        reconstruct.append(x)
    return reconstruct

def Test_Image(test_img,avg,eigenvector):
    test_img = Flatten(test_img)
    selisih = Selisih(avg,test_img)
    weight = Weight(eigenvector,selisih)
    return weight

def euclideanDistance(omega_t,omega_d):
    ed = []
    for i in range(len(omega_d)):
        temp = np.subtract(omega_t[0],omega_d[i])
        sum_sq = np.dot(np.transpose(temp),temp)
        ed.append(np.sqrt(sum_sq))
    return ed

def Eigenfaces(m,test_image):
    start = time.time()
    m = Flatten(m)
    average = Average(m)
    selisih = Selisih(average,m)
    covarian = Covarian(selisih)

    # eigenvector = (EigenvectorAtA(covarian))
    # eigenvector = EigenvectorAAt(eigenvector,selisih)
    # eigenvector = normalizeEigenVector(eigenvector)
    # eigenvector = eigenvector[:len(eigenvector)//2]

    [eigenvalue,eigenvector] = eigen.eigenalgorithm(covarian)
    eigenvector = normalizeEigenVector(eigenvector)
    eigenvector = EigenvectorAAt(eigenvector,selisih)
    eigenvector = normalizeEigenVector(eigenvector)


    omega_d = Weight(eigenvector,selisih)
    omega_t = Test_Image(test_image,average,eigenvector)
    ed = euclideanDistance(omega_t,omega_d)
    id = np.argmin(ed)
    end = time.time()
    execution_time = end-start
    img = Unflatten(m)[id]

    return (img,execution_time,ed[id]<=10000)