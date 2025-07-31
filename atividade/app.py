from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/imc', methods=['GET','POST'])
def imc():
    if request.method == 'GET':
        return render_template('imc.html')
    if request.method == 'POST':
        nome = request.form.get('nome')
        genero = request.form.get('genero')
        altura = request.form.get('alt')
        peso = request.form.get('peso')
        int(altura)
        int(peso)
        dados = {
            'nome':nome,
            'genero':genero,
            'altura':altura,
            'peso':peso
        }
        return render_template('ImcResult.html', dados = dados)


app.run(debug=True)
