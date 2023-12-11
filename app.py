doenças = {
    'gripe': {
        'sintomas': ['febre', 'tosse', 'dor de cabeca']
    },
    'catapora': {
        'sintomas': ['manchas vermelhas', 'coceira', 'febre']
    }
    # Adicione mais doenças conforme necessário
}

from flask import Flask, jsonify  # Adicione jsonify aqui

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/doencas')
def listar_doencas():
    return jsonify(doenças)  # Isso irá funcionar agora que você importou jsonify

if __name__ == '__main__':
    app.run()
