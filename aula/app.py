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
        telefone = request.form.get('num')
        data = request.form.get('d')
        hora = request.form.get('h')
        servico = request.form.get('service')
        
        dados = {
                'nome':nome, 
                'email':email, 
                'telefone':telefone, 
                'data':data, 
                'hora':hora, 
                'servico':servico
            }
        
        if nome == 'Huygnes' or 'huygnes':
            if email == 'huygnes@gmail.com':
                return render_template('segredo.html')
        print('metodo POST utilizado', nome, email)
        return render_template('ConfServico.html', dados = dados)
app.run(debug=True)