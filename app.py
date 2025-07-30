from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'GET':
        print('metodo GET utilizado')
        return render_template('agendar.html')
    elif request.method == 'POST':
        nome = request.form.get('n')
        email = request.form.get('e')
        if nome == 'Huygnes' or 'huygnes':
            if email == 'huygnes@gmail.com':
                return render_template('segredo.html')
        print('metodo POST utilizado', nome, email)
        return render_template('agendar.html', nome = nome, email = email)
    
app.run(debug=True)