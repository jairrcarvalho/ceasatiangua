from flask import Flask,render_template,request
from resquets_ceasa import obterConsulta, dataTabela

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/teste', methods=['POST'])
def teste():
    dados = request.get_json()
    nome_legume = dados['conteudo']
    url = dados['url']
    consulta = obterConsulta(url,nome_legume)
    
    return f'{consulta}'

@app.route('/data', methods = ['POST'])
def data():
    return dataTabela()



if __name__ == '__main__':
    app.run(debug=True)
