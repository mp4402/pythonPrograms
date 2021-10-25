from flask import Flask, render_template

class Persona:
    def __init__(self,Nombre,Edad,Carrera,Hobbie):
        self.nombre = Nombre
        self.edad = Edad
        self.carrera = Carrera
        self.hobbie = Hobbie

app = Flask(__name__)

@app.route('/index')
def renderTemplate():
    body = "Este es el body de index"
    lista = [1,2,3,4,5]
    return render_template("index.html",body=body,my_list=lista)

@app.route('/')
def describirPersona():
    descripcion = f"Nombre: {mario.nombre} Edad: {mario.edad} Carrera: {mario.carrera} Hobbie: {mario.hobbie}"
    return f"{descripcion}"

@app.route('/nombre')
def decirNombre():
    return f"{mario.nombre}"

@app.route('/edad')
def decirEdad():
    return f"{mario.edad}"

@app.route('/carrera')
def decirCarrera():
    return f"{mario.carrera}"

@app.route('/hobbie')
def decirHobbie():
    return f"{mario.hobbie}"

if (__name__ == '__main__'):
    mario = Persona("Mario Enrique Pisquiy Gómez","18","Computer Science", "Escuchar Música")
    app.run()


