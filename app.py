from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para receber uma requisição POST
@app.route('/api/receber_dados', methods=['GET'])
def receber_dados():
    # Obter dados do corpo da requisição JSON
    # dados = request.get_json()
    dados = request.args.get('teste')
    # Processar os dados (neste exemplo, apenas imprimir)
    print("Dados recebidos:", dados)

    # Responder com uma mensagem de sucesso
    return jsonify({"mensagem": "Dados recebidos com sucesso!"})

if __name__ == '__main__':
    # Executar o aplicativo na porta 5000 por padrão
    app.run(debug=True)
