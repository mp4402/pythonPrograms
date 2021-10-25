from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader

file_loader = FileSystemLoader("templates")
env = Environment(loader = file_loader)

app = Flask(__name__)

output = [""]

def reverse(cadena):
    nCadena = ""
    for n in cadena:
        nCadena = n + nCadena
    output[0] = nCadena

def longitud(cadena):
    largoCadena = len(cadena)
    str(largoCadena)
    output.append(largoCadena)

def vowelsConsonants(cadena):
    vocal = 0
    consonante = 0
    carAsc = 0
    vocales = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
    consonantes = [66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 98, 99, 100, 102, 103, 104, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122]
    for n in cadena:
        carAsc = ord(n)
        for m in vocales:
            if carAsc == m:
                vocal += 1

        for x in consonantes:
            if carAsc == x:
                consonante += 1

    str(vocal)
    str(consonante)
    output.append(vocal)
    output.append(consonante)

def upper(cadena):
    upCadena = cadena.upper()
    output.append(upCadena)

def lower(cadena):
    lowCadena = cadena.lower()
    output.append(lowCadena)

def upDown(cadena):
    nuevaCadena = ""
    contador = 0
    for n in cadena:
        contador += 1
        if (contador % 2 != 0):
            n = n.upper()
        nuevaCadena += n
    output.append(nuevaCadena)

def naive(cadena):
    nuevaCadena = ""
    for n in cadena:
        if n == "a" or n == "A":
            n = "@"
        elif n == "e" or n == "E":
            n = "3"
        elif n == "i" or n == "I":
            n = "!"
        elif n == "o" or n == "O":
            n = "0"
        elif n == "u" or n == "U":
            n = ")"
        else:
            n = n
        nuevaCadena += n
    output.append(nuevaCadena)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        _input = request.form['input']
        reverse(_input)
        longitud(_input)
        vowelsConsonants(_input)
        upper(_input)
        lower(_input)
        upDown(_input)
        naive(_input)
        template = env.get_template("index.html")
        return template.render(my_list = output, image = "static\\avatar.jpg")
    template = env.get_template("index.html")
    return template.render(image = "static\\avatar.jpg")

if __name__ == "__main__":
    app.run()