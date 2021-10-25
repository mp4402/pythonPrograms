from flask import Flask, request, redirect, url_for, render_template, jsonify
from jinja2 import Template, Environment, FileSystemLoader
import yaml
import os,optparse,sys

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

app = Flask(__name__)
with open("informacion.yaml") as yaml_file:
    my_yaml = yaml.load(yaml_file)
    print(my_yaml["fotografia"])

@app.route("/cv")
def cv():
    template = env.get_template("cv.html")
    image_file = url_for("static", filename=my_yaml["fotografia"])
    return template.render(my_data=my_yaml,image_file = image_file)

@app.route("/links")
@app.route("/")
def home():
    foo="bar"
    return render_template("index.html", links=my_yaml["links"], developer = "Mario Pisquiy")

if __name__ == "__main__":
    app.run()