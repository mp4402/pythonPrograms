from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json 

file_loader = FileSystemLoader("templates")
env = Environment(loader = file_loader)

app = Flask(__name__)
with open("data.json") as json_file:
    my_json = json.load(json_file)

@app.route("/")
def index():
    template = env.get_template("index.html")
    return template.render(my_data=my_json["data"], headers=my_json["headers"])

@app.route("/crear", methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        _id = request.form["id"]
        _type = request.form["type"]
        _name = request.form["name"]
        _quantity = request.form["quantity"]
        
        my_json["data"].append({"id":_id,"type":_type,"name":_name,"quantity":_quantity})
        return redirect(url_for("index"))

    template = env.get_template("form.html")
    return template.render()

if __name__ == "__main__":
    app.run()