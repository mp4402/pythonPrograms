def particion(inicio, fin, array):
	
	indicePivote = inicio
	pivot = array[indicePivote]
	
	while inicio < fin:
		
		while inicio < len(array) and array[inicio] <= pivot:
			inicio += 1
			
		while array[fin] > pivot:
			fin -= 1
		
		if(inicio < fin):
			array[inicio], array[fin] = array[fin], array[inicio]
	
	array[fin], array[indicePivote] = array[indicePivote], array[fin]
	
	return fin
	
def quick_sort(inicio, fin, array):
	
	if (inicio < fin):
		p = particion(inicio, fin, array)

		quick_sort(inicio, p - 1, array)
		quick_sort(p + 1, fin, array)

array = [ 10, 7, 8, 9, 1, 5 ]
print(f'Lista sin ordenar: {array}')
quick_sort(0, len(array) - 1, array)

print(f'Lista ordenada: {array}')