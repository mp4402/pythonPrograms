#Mario Enrique Pisquiy Gómez	Carné 20200399
def multiplicacionKayatsuba(n1,n2):
    if len(str(n1)) == 1 or len(str(n2)):
        return n1 * n2
    else:
        n = max(len(str(n1)),len(str(n2)))
        n_2 = int(n/2)
        a = int(str(n1)[0,n_2])
        c = int(str(n2)[0,n_2])
        ac = multiplicacionKayatsuba(a,c)
        b = int(str(n1)[n_2,len(n1)])
        d = int(str(n2)[n_2,len(n1)])
        bd = multiplicacionKayatsuba(b,d)
        suma = multiplicacionKayatsuba(a+b,c+d) - ac - bd
        return ac * (10^(2*n_2)) + (suma*(10^n_2)) + bd

n1 = int(input(""))
n2 = int(input(""))
print(multiplicacionKayatsuba(n1, n2))