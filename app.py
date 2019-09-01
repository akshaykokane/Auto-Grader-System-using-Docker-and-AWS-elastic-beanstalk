from flask import Flask, render_template
import random

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html', url=url)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
   return "file uploaded successfully. AUTOGRADING IN PROGRESS.."
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
