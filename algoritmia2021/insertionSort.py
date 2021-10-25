def insertionSort(arr):
	if len(arr)<=1:
		return
	
	insertionSort(arr)
	val = arr[len(arr)-1]
	pos = len(arr)-2
	while (pos>=0 and arr[pos]>val):
		arr[pos+1] = arr[pos]
		pos = pos-1

	arr[pos+1]=val

arr = [12,11,13,5,6]
insertionSort(arr)
