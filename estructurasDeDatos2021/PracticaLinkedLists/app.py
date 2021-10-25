from memory_profiler import profile
from flask import Flask, request
from jinja2 import Template, Environment, FileSystemLoader
import csv
import cProfile
class Cancion:
    def __init__(self, nombre, artista, album):
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.previous = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    @profile
    def insertar(self,nombre,artista,album):
        nuevaCancion = Cancion(nombre,artista,album)
        nuevaCancion.next = None
        if self.head is None:
            self.head = nuevaCancion
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = nuevaCancion
        nuevaCancion.previous = last
        return

    @profile
    def recorrer(self,cancion):  
        global last      
        while (cancion is not None):
            print(cancion.nombre,cancion.artista,cancion.album),
            last = cancion
            cancion = cancion.next   

@profile
def añadirCancion(nombre,artista,album)-> None:
    datos = ["","",""]
    datos[0] = nombre
    datos[1] = artista
    datos[2] = album
    with open('listado.csv','a',newline='') as writeFile:
        writer = csv.writer(writeFile,delimiter=",",quotechar=',',quoting=csv.QUOTE_MINIMAL,lineterminator='')
        writer.writerow('\n')
        writer.writerow(datos)
    listaCanciones.append(Cancion(datos[0],datos[1],datos[2]))
    listadoCanciones.insertar(datos[0],datos[1],datos[2])

@profile
def cargarCanciones():
    global listadoCanciones
    with open('listado.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            datos = row
            #if contador == 0:
            #    listadoCanciones.push(datos[0],datos[1],datos[2])
            #else:
            listaCanciones.append(Cancion(datos[0],datos[1],datos[2]))
            listadoCanciones.insertar(datos[0],datos[1],datos[2])

listadoCanciones = LinkedList()
listaCanciones = []
cargarCanciones()
cancionActual = listadoCanciones.head

File_loader = FileSystemLoader("templates")
env = Environment(loader=File_loader)
app = Flask(__name__)

@app.route('/', methods=["GET","POST"], endpoint='index')
@profile
def index():
    global cancionActual, listadoCanciones
    contador = 0 
    if(request.method == "POST"):
        if request.form.get('Play Previous') == 'Play Previous':
            if(cancionActual.previous is None):
                pass
            else:
                cancionActual = cancionActual.previous
        elif request.form.get('Play Next') == 'Play Next':
            if(cancionActual.next is None):
                pass
            else:
                cancionActual = cancionActual.next
        else:
            pass
        template = env.get_template('index.html')
        return template.render(nombreCancion=cancionActual.nombre,nombreArtista=cancionActual.artista,nombreAlbum=cancionActual.album )
    template = env.get_template('index.html')
    return template.render(nombreCancion="---",nombreArtista="---",nombreAlbum="---")

@app.route('/añadir', methods=["GET","POST"], endpoint='añadir')
@profile
def añadir():
    if(request.method == "POST"):
        nombre = request.form['var1']
        artista = request.form['var2']
        album = request.form['var3']
        añadirCancion(nombre,artista,album)
    template = env.get_template('añadir.html')
    return template.render()

@app.route('/listar', endpoint='listar')
@profile
def listar():
    #limpiarListado()
    #cargarCanciones()
    template = env.get_template('listar.html')
    return template.render(my_list=listaCanciones)

if __name__ == '__main__':
    app.run()

cProfile.run("insertar('The Show Must Go On','Queen','Innuendo')")
cProfile.run("recorrer(listadoCanciones.head")
cProfile.run("añadirCancion('The Show Must Go On','Queen','Innuendo')")
cProfile.run("cargarCanciones()")