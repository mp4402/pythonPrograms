import time
import random
class  IntegratedCircuit:
    correlativo = 0
    listatus = ["production", "development", "deprecated"]
    lisstock = [100, 50, 0]
    meses = ["","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio","Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    def __init__(self, manufacturer,country,  description):
        numero = random.randrange(0,2)
        self.tiempo = time.gmtime()
        self.status = self.listatus[numero]
        self.stock = self.lisstock[numero]
        self.manufac = manufacturer
        self.coun = country
        self.descrip = description
        self.serial = self.manufac[0].upper()
        for i in range(len(self.manufac)):
            if (self.manufac[i] == " "):
                self.serial += self.manufac[i+1].upper()
        self.serial += "-"
        self.serial += self.coun[0].upper()
        for i in range(len(self.coun)):
            if (self.coun[i] == " "):
                self.serial += self.coun[i+1].upper()
        IntegratedCircuit.correlativo = IntegratedCircuit.correlativo + 1 
        self.serial += "-"
        self.serial += str(IntegratedCircuit.correlativo)
    def To_String(self):
        if(self.status == "deprecated"):

            print(f"La manufactura es {self.manufac}, fecha: {self.tiempo.tm_mday}, {self.meses[tiempo.tm_mon]}, {self.tiempo.tm_year} su ciudad es {self.coun}, con status {self.status}, su stock {self.stock}\n")
        else:
            print(f"La manufactura es {self.manufac}, fecha: {self.tiempo.tm_mday}, {self.meses[self.tiempo.tm_mon]}, {self.tiempo.tm_year}, su ciudad es {self.coun}, con descrición de {self.descrip}, con status {self.status}, su stock {self.stock}\n")
    def getSerial(self):
        print(f"Su serial es: {self.serial}")
        #print(f"{type(self.serial)}")
    def getSerialNo(self):
        punto = 0
        for i in range(len(self.serial)):
            if self.serial[i] == "-":
                punto = i+1
        print(f"El número correlativo de la instancia es: {self.serial[punto:]}")
    def Total():
        print(f"La cantidad total de IntegratedCircuit: {IntegratedCircuit.correlativo}")
    def getStatus(self):
        print(f"{self.status}")
    def ChangeStatus(self, num):
        self.status = self.listatus[num]
        self.stock = self.lisstock[num]
    def getStock(self):
        return self.stock
    def addStock(self, i):
        self.stock = self.stock + i
    def subStock(self, i):
        self.stock = self.stock - i
        if(self.stock < 0):
            self.stock = 0
    def updateStock(self, i):
        if(i < 0):
            pass
        else:
            self.stock = i

instancia1 = IntegratedCircuit("International Business Machines", "Estados Unidos", "Circuito de apple")
instancia1.To_String()
instancia1.getSerial()
instancia1.getSerialNo()
instancia1.ChangeStatus(1)
instancia1.getStock()
instancia1.addStock(50)
instancia1.getStatus()
instancia1.subStock(45)
instancia1.updateStock(50)
stockfinal = instancia1.getStock()
print(f"El stock final de la instancia1 es: {stockfinal}")
instancia2 = IntegratedCircuit("Circitos Integrados", "Republica Dominicana", "Circuito Google")
instancia2.To_String()
instancia2.getSerial()
instancia2.getSerialNo()
instancia2.ChangeStatus(2)
instancia2.getStock()
instancia2.addStock(-10)
instancia2.getStatus()
instancia2.subStock(-45)
instancia2.updateStock(100)
stockfinal = instancia2.getStock()
print(f"El stock final de la instancia2 es: {stockfinal}")
instancia3 = IntegratedCircuit("Agregados Ver Total", "Guatemala", "Para mostrar que hay más correltativos")
instancia3.To_String()
IntegratedCircuit.Total()

