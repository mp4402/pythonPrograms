import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from jinja2 import FileSystemLoader, Environment

UPLOAD_FOLDER = 'C:/Users/mepg1/Documents/GitHub/pythonPrograms/flaskPrograms/pruebaUploads/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

File_loader = FileSystemLoader("templates")
env = Environment(loader=File_loader)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    template = env.get_template('index.html')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return template.render()
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return template.render(mensaje="No se seleccionó ninguna imagen")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return template.render(mensaje="Imagen subida correctamente")
    return template.render(mensaje="")

if __name__ == '__main__':
    app.run(debug=True)