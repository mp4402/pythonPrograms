def merge(C, D): 
    i = 0
    j = 0
    lenC = len(C)
    lenD = len(D)
    n = lenC + lenD
    B = []
    iband = True
    for k in range(n):
        if j == lenD or iband and C[i][0] < D[j][0]: 
            B.append(C[i])
            i+=1  
            if i == lenC: 
                iband = False 
        elif j < lenD: 
            B.append(D[j])
            j+=1
    return B

def merge_sort(A):
    n = len(A)
    if n == 1: 
        return A
    else: 
        mitad = int(n/2)
        list1 = A[:mitad]
        list2 = A[mitad:]
        C = merge_sort(list1)
        D = merge_sort(list2)
        return merge(C,D)


def unir(B, C): 
    D = []
    i = []
    for i in B: 
        D.append(i)
    last = i # ültimo elemento de la lista izquierda
    first = C[0] # primer elemnto de la lista derecha 
    for i in C: 
        D.append(i)
    last_left = i

    d = (last[0]-first[0])**2 + (last[1]-first[1])**2 # Calcula la distancia al cuadrados del último punto de lado izquierdo
    return D, d, [last,first]                         # y el primer punto del lado derecho. 

def divide(A):
    n = len(A)
    if n <= 1:
        d = float("inf")
        return A, d,[A,A]
    elif n == 2:
        d = (A[0][0]-A[1][0])**2 + (A[0][1]-A[1][1])**2 # calcula la distancia al cuadrada entre dos puntos 
        return A, d, A
    else: 
        mitad = int(n/2)
        list1 = A[:mitad]
        list2 = A[mitad:]
        left,d1,pl = divide(list1) # pl: pareja de puntos más cercanos de la izquierda
        righ,d2,pr = divide(list2) # pr: pareja de puntos más cercanos de la derecha 
        lista,d3,pc = unir(left, righ) # pc: pareja de puntos del centro 

        dmin = 0 # Distancia minima entre los puntos más cercanos
        p = [] # pareja de puntos más cercanos 
        if d1 < d2:
            # print("d1 < d2") 
            dmin = d1
            p = pl
        else:
            # print("d1 > d2")
            dmin = d2
            p = pr
        if d3 <= dmin: 
            # print("d3 <= dmin") 
            dmin = d3 
            p = pc
        
        return lista, dmin, p # Retorna la lista, la distancia y los puntos más cercanos 
        

ls = [[1,2], [2, 3], [3, 3], [3 , 3.5]]

ls,d,pr =divide(ls)
print("Lista de puntos:",ls)
print("Puntos mas cercanos:",pr)
print("Distancia:",d**(0.5))


print()
lista = [[10,10], [1, 2], [5,6], [7,3], [4,9], [1,2.5], [5.5, 6]]
lista = merge_sort(lista)
print("Merge Sort Result: ", lista)

print()
lista,d,pr = divide(lista)
print("Lista de puntos:", lista)
print("Puntos mas cercanos:",pr) 
print("Distancia:",d**(0.5))
