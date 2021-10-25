#código de Merge Sort
from random import randint
def Mergesort(A):
  n = len(A)
  if n == 1:
    return A
  else:
    mitad = n//2
    PA1 = A[0:mitad]
    PA2 = A[mitad:]
    c = Mergesort(PA1)
    d = Mergesort(PA2)
    return Merge(c,d)

def Merge(c,d):
  i = 0
  j = 0
  n = len(c) + len(d)
  lenC = len(c)
  lenD = len(d)
  #print(lenC)
  #print(lenD)
  B = []
  ibandera = 0
  jbandera = 0
  for k in range(n):
    if (c[i] < d[j] and ibandera == 0) or jbandera == 1:
      B.append(c[i])
      i = i + 1
      if i >= lenC:
        i = i - 1
        ibandera = 1
      #print("Entreal de c[i] < d[j]")
    else:
      B.append(d[j])
      j = j + 1
      if j >= lenD:
        j = j - 1
        jbandera = 1
      #print("Entreal de c[i] > d[j]")
  return B
# generate some integers
A = []
n= 10
while(n != 1):
  value = randint(1, 50)
  print(type(value))
  A.append(value)
  n = n - 1
print(len(A))
print(A)

B = Mergesort(A)
print(B)

#INVERSIONES

inversiones = 0
def INVERSION(A):
  n = len(A)
  if n == 1:
    return A
  else:
    mitad = n//2
    PA1 = A[0:mitad]
    PA2 = A[mitad:]
    c = INVERSION(PA1)
    d = INVERSION(PA2)
    return Merge2(c,d)

def Merge2(c,d):
  global inversiones
  i = 0
  j = 0
  n = len(c) + len(d)
  lenC = len(c)
  lenD = len(d)
  #print(lenC)
  #print(lenD)
  B = []
  ibandera = 0
  jbandera = 0
  countinversion = 0
  for k in range(n):
    if (c[i] <= d[j] and ibandera == 0) or jbandera == 1:
      B.append(c[i])
      i = i + 1
      if i >= lenC:
        i = i - 1
        ibandera = 1
      #print("Entreal de c[i] < d[j]")
    else:
      B.append(d[j])
      if ibandera == 0:
        x = lenC - i
        countinversion = countinversion + x
      j = j + 1
      if j >= lenD:
        j = j - 1
        jbandera = 1
      #print("Entreal de c[i] > d[j]")
  inversiones = inversiones + countinversion
  #print(f"Las inversiones en merge: {inversiones}")
  #print(f"Las countinversion son: {countinversion}")
  #print(B)
  return B

A = []
n = 10
while(n != 1):
  value = randint(1, 10)
  print(type(value))
  A.append(value)
  n = n - 1
print(len(A))
print(A)
B = INVERSION(A)
print(B)
print(f"Las inversiones son: {inversiones}")