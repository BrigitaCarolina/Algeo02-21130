import numpy as np

mat = [[[2,0,1],[1,2,1],[0,2,4]],
[[1,0,2],[0,1,1],[1,2,2]],
[[1,2,3],[2,4,3],[1,2,3]]]
print(mat)

# mean training image
def mean(training_image):
    return np.mean(training_image, axis=0)

# average = mean(mat)
# print(average)

# selisih training image dengan mean
def Selisih(average,training_image):
    selisih = []
    for i in range(len(training_image)):
        # selisih.append(np.absolute(np.subtract(training_image[i],average)))
        selisih.append(np.subtract(training_image[i],average))
    row = len(selisih[0])*len(selisih[0][0])
    col = len(selisih)
    selisih = np.reshape(selisih,(col,row))
    selisih = np.transpose(selisih)
    return selisih

# selisih = Selisih(average,mat)
# print(selisih)

# matrix covarian
def Covarian(selisih):
    Aa = selisih
    At = np.transpose(selisih)
    # return np.matmul(At,Aa)
    return np.divide(np.matmul(At,Aa),len(selisih))

# covarian = Covarian(selisih)
# print(covarian)

def Eigenfaces(imgArr):
    average = mean(imgArr)
    selisih = Selisih(average,imgArr)
    covarian = Covarian(selisih)
    covarian = np.int_(covarian)
    print(covarian)
    (eigenvalue,eigenvector) = np.linalg.eig(covarian)
    eigenface = np.matmul(eigenvector,np.transpose(selisih))
    eigenface = np.reshape(eigenface,(-1,256,256))
    return eigenface