from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import yaml

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

app = Flask(__name__)
with open("informacion.yaml") as yaml_file:
    my_yaml = yaml.load(yaml_file)
    print(my_yaml["fotografia"])

@app.route("/")
def mostrarIndex():
    template = env.get_template("index.html")
    image_file = url_for("static", filename=my_yaml["fotografia"])
    return template.render(my_data=my_yaml,image_file = image_file)

if __name__ == "__main__":
    app.run()