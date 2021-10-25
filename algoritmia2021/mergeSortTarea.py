countInversiones = 0
def sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array)//2
        mid1 = array[:mid]
        mid2 = array[mid:]
        C = sort(mid1)
        D = sort(mid2)
        return merge(C,D)

def merge(C,D):
    i=0
    j=0
    k=0
    n = len(C) + len(D)
    lenC = len(C)
    lenD = len(D)
    banderaI = 0
    banderaJ = 0
    B=[]
    for k in range(n):
        if (C[i] < D[j] and banderaI== 0) or banderaJ == 1:
            B.append(C[i])
            i += 1
            if i >= lenC:
                i-=1
                banderaI = 1
        else:
            B.append(D[j])
            j += 1
            if j >= lenD:
                j-=1
                banderaJ = 1
    return B

def inversiones(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array)//2
        mid1 = array[:mid]
        mid2 = array[mid:]
        C = inversiones(mid1)
        D = inversiones(mid2)
        return contarInversiones(C,D)

def contarInversiones(C,D):
    global countInversiones
    i=0
    j=0
    n = len(C) + len(D)
    lenC = len(C)
    lenD = len(D)
    banderaI = 0
    banderaJ = 0
    inversions = 0
    B = []
    for k in range(n):
        if (C[i] <= D[j] and banderaI== 0) or banderaJ == 1:
            B.append(C[i])
            i += 1
            if i >= lenC:
                i-=1
                banderaI = 1
        else:
            B.append(D[j])
            if banderaI == 0:
                x = lenC - i
                inversions += x
            j += 1
            if j >= lenD:
                j-=1
                banderaJ = 1
    countInversiones += inversions
    return B

array=[1,5,8,10,3,6,8,1]
print(array)
noInversiones = inversiones(array)
print("El número de inversiones es: " + str(countInversiones))
array=sort(array)
print(array)