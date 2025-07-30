from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/agendar')
def agendar():
    return render_template('agendar.html')
app.run(debug=True)