import random
def quickSort(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        p=choosePivote(arr)
        i=rearrange(arr,p)
        quickSort(arr[1:i-1])
        quickSort(arr[i+1:n])

def choosePivote(arr):
    n = len(arr)
    return random.randint(1,n)


def rearrange():
    pass