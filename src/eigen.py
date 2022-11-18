import numpy as np

mat = [[5,6,3,4],
       [5,2,0,3],
       [2,4,5,2],
       [5,11,9,2]]

mat2 = [[1,7,3],[2,1,2],[3,8,3]]

matset = [[1, 2, 3, 7],
          [0, 4, 5, 8],
          [0, 0, 6, 9],
          [0, 0, 0, 11]]

def dot(a,b):
    dprod = 0
    size = len(a)
    for i in range(size):
        dprod += (a[i]*b[i])
    
    return dprod

def magnitude(a):
    suma = 0
    for i in range(len(a)) :
        suma += pow(a[i],2)
    maga = np.sqrt(suma)

    return maga

def qr(matrix):
    sizei = len(matrix)
    sizej = len(matrix[0])
    a = []
    u = [[]] * sizei
    e = []

    for j in range(sizej) :
        tempa = []
        for i in range(sizei) :
            tempa.append(matrix[i][j])
        a.append(tempa)
    
    for i in range(sizei) :
        u[i] = a[i]
        for ie in range(len(e)):
            u[i] -= dot(a[i],e[ie])*e[ie]
        e.append(u[i] / magnitude(u[i]))
    
    q = [0] * sizei
    for i in range(sizei) :
        q[i] = e[i]
    q = np.transpose(q)
    
    r = []
    for i in range(sizei) :
        temp = [0] * sizei
        for j in range(sizej) :
            temp[j] = dot(e[i],a[j])
        r.append(temp)

    for i in range(sizei) :
        for j in range(i) :
            r[i][j] = 0
    
    decom = [q,r]

    return decom

def segitigaatas_checker(matrix):
    isTrue = True

    sizei = len(matrix)
    sizej = len(matrix[0])

    if sizei != sizej :
        isTrue = False
    else :
        for i in [1, sizei-1] :
            for j in range(i) :
                if matrix[i][j] != 0:
                    isTrue = False
    
    return isTrue

def identitymaker(a):
    identity = []

    for i in range(a):
        add=[]
        for j in range (a):
            if i != j :
                add.append(0)
            else :
                add.append(1)
        identity.append(add)
    
    return identity


def givenrotation(m, i, j):
    rotation = []

    a = len(m)

    for k in range(a):
        add=[]
        for l in range (a):
            if k != l :
                add.append(0)
            else :
                add.append(1)
        rotation.append(add)
    
    p = m[i][i]
    q = m[j][i]
    r = np.sqrt(pow(p,2) + pow(q,2))

    a = p/r
    b = np.sqrt(1-pow(a,2))

    rotation[i][i] = a
    rotation[j][j] = a
    rotation[i][j] = b
    rotation[j][i] = -b
    
    return rotation

def heissenberg(matrix):
    sizei = len(matrix)
    for i in [1, (sizei-2)] :
        for j in [i+1, (sizei-1)] :
            g = givenrotation(matrix,i,j)
            gt = np.transpose(g)
            matrix = np.matmul(np.matmul(g,matrix),gt)
            matrix[j][i-1] = 0
            
    return matrix

def diagonal(matrix):
    diagonals = []

    for i in range(len(matrix)) :
        diagonals.append(matrix[i][i])
    
    return diagonals


def eigenvalue(matrix):
    f = len(matrix)
    H = heissenberg(matrix)
    E = diagonal(H)
    I = identitymaker(f)
    Q = I

    while segitigaatas_checker(H) == False :
        qrmat = qr(H)
        q = qrmat[0]
        Q = np.matmul(q,Q)
        r = qrmat[1]
        H = np.matmul(r, q)
        E = diagonal(H)
    
    v = []
    for i in range(f):
        temp = E[i]*np.array(I)
        temph = np.array(matrix) - temp
        parameters = []
        for j in range(f):
            parameters.append(-temph[j][f-1])
            np.delete(temph[j],f-1,0)
        np.delete(temph,f-1,0)
        v.append(np.linalg.solve(temph,parameters))
        
        
    return [E,v]

print(eigenvalue(mat2))
