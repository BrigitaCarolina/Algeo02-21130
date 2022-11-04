import numpy as np

mat = [[[2,0,1],[1,2,1],[0,2,4]],
[[1,0,2],[0,1,1],[1,2,2]],
[[1,2,3],[2,4,3],[1,2,3]]]
print(mat)

# mean training image
def mean(training_image):
    return np.mean(training_image, axis=0)

average = mean(mat)
print(average)

# selisih training image dengan mean
def Selisih(average,training_image):
    selisih = []
    for i in range(len(training_image)):
        selisih.append(np.absolute(np.subtract(training_image[i],average)))
    return selisih

selisih = Selisih(average,mat)
print(selisih)

# matrix covarian
def Covarian(selisih):
    Aa = np.concatenate(selisih,axis=1)
    At = np.transpose(Aa)
    return np.matmul(Aa,At)

covarian = Covarian(selisih)
print(covarian)

