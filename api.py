#from crypt import methods
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/admin')
def panel():
    return render_template('denied.html')

@app.route('/api',methods=['GET'])
def metoda():
    return render_template('denied.html')
@app.route('/api',methods=['POST'])
def flaga():
    return "Brawo Flaga CTF{Fl4G_Brav0_S13M4}"
@app.route('/flag')
def fake():
    return "Nie tak łatwo!"


if __name__ == "__main__":    
    app.run(port=9001)