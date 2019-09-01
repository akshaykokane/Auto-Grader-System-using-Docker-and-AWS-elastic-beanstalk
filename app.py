from flask import Flask, render_template, request
from werkzeug import secure_filename
from exe import autoGrade

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
   return autoGrade();
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
