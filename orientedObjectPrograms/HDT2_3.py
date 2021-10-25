import time
import random
NoSerial = 0
class IntegratedCircuit:
    meses = ["","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    def __init__(self,manufacturer, country, description, status, stock,date,serial):
        self.manufacturer = manufacturer
        self.country = country
        self.description = description
        self.status = status
        self.stock = stock
        self.date = time.gmtime()
        self.serial = serial
    
    def statusStock(self)->None:
        x = random.randint(0,2)
        if (x == 0):
            self.status = "Production"
            self.stock = 100
        elif (x==1):
            self.status = "Development"
            self.stock = 50
        else:
            self.status = "Deprecated"
            self.stock = 0

    
    
    def getSerialNo():
        global NoSerial
        NoSerial +=1
        return str(NoSerial)

    def getSerial(self):
        indice = 0
        serial = ""
        while (indice < 3):
            serial += self.manufacturer[indice]
            indice+=1
        serial += "-" + self.country[0] 
        indice = 0
        while(indice<len(self.country)):
            if (self.country[indice]==" "):
                serial += self.country[indice+1]
                indice = len(self.country)
            indice+=1
        serial += "-" + IntegratedCircuit.getSerialNo()
        return serial.upper()

    def imprimir(self):
        if(self.status=="Deprecated"):
            return"Fabricado por {}, en {}, el {} de {} del {}. Su serial es {}, su estado es {} y su stock es {}".format(self.manufacturer, self.country, self.date.tm_mday,self.meses[self.date.tm_mon],self.date.tm_year, self.serial,self.status,self.stock)
        else:
            return"El circuito integrado es {}, fabricado por {}, en {}, el {} de {} del {}. Su serial es {}, su estado es {} y su stock es {}".format(self.description, self.manufacturer,self.country,self.date.tm_mday,self.meses[self.date.tm_mon],self.date.tm_year,self.serial,self.status,self.stock)

    def getTotal():
        return NoSerial

    def getStatus(self):
        return self.status
    
    def changeStatus(self,nuevoStatus):
        if (nuevoStatus == 0):
            self.status = "Deprecated"
            self.stock = 0
        elif (nuevoStatus==1):
            self.status = "Development"
        elif (nuevoStatus==2):
            self.status = "Production"
    
    def getStock(self):
        return self.stock

    def addStock(self,añadirStock):
        self.stock += añadirStock
    
    def subStock(self,restarStock):
        self.stock -= restarStock
        if (self.stock < 0):
            self.stock = 0
    
    def updateStock(self,nuevoStock):
        if(nuevoStock >= 0):
            self.stock = nuevoStock

Circuito1 = IntegratedCircuit("Arduino","Unites States","Arduino UNO","",0,0,"")
Circuito2 = IntegratedCircuit("Raspberry","Mexico","Raspberry UNO","",0,0,"")
Circuito1.statusStock()
Circuito2.statusStock()
Circuito1.serial = Circuito1.getSerial()
Circuito2.serial = Circuito2.getSerial()
print(Circuito1.imprimir())
print(Circuito2.imprimir())