#Mario Enrique Pisquiy Gómez
"20200399"

def encontrarPunto(IP):
    pos = IP.find(".")
    return pos

def recortarIP(IP, pos):
    IP = IP[pos+1:len(IP)]
    return IP

IP = input("Ingrese una IP: ")
IPprint = IP
tipo = ""
clase = ""

posPunto = encontrarPunto(IP)
print(posPunto)
if posPunto != -1:
    octeto1 = IP[0:posPunto]
    IP = recortarIP(IP, posPunto)
else:
    print("Ingrese una IP valida")
    raise SystemExit()

posPunto = encontrarPunto(IP)
if posPunto != -1:
    octeto2 = IP[0:posPunto]
    IP = recortarIP(IP, posPunto)
else:
    print("Ingrese una IP valida")
    raise SystemExit()

if int(octeto1) >= 0 and int(octeto1) <= 126:
    tipo = "Publica"
    clase = "A"
    if int(octeto1) == 10:
        tipo = "Privada"
elif int(octeto1) >= 128 and int(octeto1) <= 191:
    tipo = "Publica"
    clase = "B"
    if int(octeto1) == 172 and int(octeto2) >= 16 and int(octeto2) <= 31:
        tipo = "Privada"
elif int(octeto1) >= 192 and int(octeto1) <= 223:
    tipo = "Publica"
    clase = "C"
    if int(octeto1) == 192 and int(octeto2) == 168:
        tipo = "Privada"
elif int(octeto1) >= 224 and int(octeto1) <= 239:
    tipo = "Publica"
    clase = "D"
elif int(octeto1) >= 240 and (octeto1) <= 254:
    tipo = "Publica"
    clase = "E"

print("La IP " + IPprint + " es una IP " + tipo + " de clase " + clase)
