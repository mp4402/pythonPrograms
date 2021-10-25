#Mario Enrique Pisquiy Gómez    
#Carné 20200399

def productoSumasPositivos(n,x):
    if x==0:
        return 0
    else:
        return n+productoSumasPositivos(n,x-1)

def recursividadCuadrado(b):
    return productoSumasPositivos(b,b)

def insertionSort(arr,n):
	if n<=1:
		return
	
	insertionSort(arr,n-1)
	val = arr[n-1]
	pos = n-2
	while (pos>=0 and arr[pos]>val):
		arr[pos+1] = arr[pos]
		pos = pos-1

	arr[pos+1]=val

def binarySearch(array,l,n):
    if n >= l:
        mid = l + (n-1)//2
        print("mid: " + str(mid))
        print("A[mid]: " + str(array[mid]))
        if array[mid] == mid:
            print("Si se cumple A[i]==i, el valor es: " + str(mid))
            return mid
        elif array[mid] > mid:
            return binarySearch(array,l,mid-1)
        else:
            return binarySearch(array,mid+1,n)
    else:
        print("No se cumple A[i] == i")
        return-1

print("El resultado es: " + str(recursividadCuadrado(int(input("Ingrese un valor para calcular su potencia al cuadrado: ")))))
arr = [12,3,2,5,6,8,1,6,8,10]
insertionSort(arr,len(arr))
print("Resultado de insertion sort: ")
print(arr)
binarySearch(arr,0,len(arr)-1)