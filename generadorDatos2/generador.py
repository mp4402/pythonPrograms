import pandas as pd
from random import randint, random

nombres = ["Carlos","Leonel","Lucia","Maria","Juan","Jose","Adriana","Gabriela","Marcelo","Luis","Julia","Ericka","Hugo","Javier","Nadia","Belen","Alejandro","Fernando","Ana","Sofia","Cesar","Armando","Gabriela","Esmeralda"]
apellidos = ["Lllorente","Villeda","Peralta","Behar", "Gomez","Aldana","Mazariegos","Alvarado","Anzueto","Garcia","Villatoro","Reyes","Marquez","Morales","Aragon","de Leon","Santizo","Perez","Godoy","Espinoza","Caceres","Robles"]

cuentas = pd.DataFrame(columns=['no_cuenta','nombre','apellido','saldo','tipo','estados'])
caja = pd.DataFrame(columns=['numero','cajero'])

for i in range(200):
    tipo = randint(0,1)
    if tipo == 0:
        tipoCadena = "Monetaria"
    else:
        tipoCadena = "Ahorros"
    if i < 10:
        no_cuenta = "0000"+str(i+1)
    elif i < 100:
        no_cuenta = "000"+str(i+1)
    else:
        no_cuenta = "00"+str(i+1)
    list_row = [no_cuenta,nombres[randint(0, len(nombres)-1)],apellidos[randint(0, len(apellidos)-1)], randint(1000,3000)+round(random(),2),tipoCadena,"Activa"]
    cuentas.loc[len(cuentas)] = list_row

for i in range(15):
    if i < 10:
        id_caja = "00" + str(i+1)
    else:
        id_caja = "0" + str(i+1)
    list_row = [id_caja,nombres[randint(0, len(nombres)-1)] + " " + apellidos[randint(0, len(apellidos)-1)]]
    caja.loc[len(caja)] = list_row

print(caja)

cuentas.to_csv('cuentas.csv')
caja.to_csv('caja.csv')

