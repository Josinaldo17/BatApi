from flask import Flask, redirect, render_template, jsonify
import os
import requests

app = Flask(__name__)

valid_tokens = os.environ.get('TOKENS')

@app.route('/<string:token>/cpf1/<string:cpf>', methods=['GET'])
def get_cpf1(token, cpf):
    SOURCE_URL = f'https://x-search.xyz/test-by-x-slayer/apis/batpuxadas/01/cpf.php?cpf={cpf}'  # Substitua pela URL real

    if token in valid_tokens:
        try:
            response = requests.get(SOURCE_URL)
            
            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({'error': 'Falha ao obter dados do site'}), response.status_code
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'message': 'Token inválido!'}), 401

@app.route('/<string:token>/cpf2/<string:cpf>', methods=['GET'])
def get_cpf2(token, cpf):
    SOURCE_URL = f'https://x-search.xyz/test-by-x-slayer/apis/batpuxadas/02/cpf.php?cpf={cpf}'  # Substitua pelo link correspondente

    if token in valid_tokens:
        try:
            response = requests.get(SOURCE_URL)
            
            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({'error': 'Falha ao obter dados do site'}), response.status_code
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'message': 'Token inválido!'}), 401

@app.route('/<string:token>/cpf3/<string:cpf>', methods=['GET'])
def get_cpf3(token, cpf):
    SOURCE_URL = f'https://x-search.xyz/test-by-x-slayer/apis/batpuxadas/03/cpf.php?cpf={cpf}'  # Substitua pelo link correspondente

    if token in valid_tokens:
        try:
            response = requests.get(SOURCE_URL)
            
            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({'error': 'Falha ao obter dados do site'}), response.status_code
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'message': 'Token inválido!'}), 401

@app.route('/<string:token>/cpf4/<string:cpf>', methods=['GET'])
def get_cpf4(token, cpf):
    SOURCE_URL = f'https://x-search.xyz/test-by-x-slayer/apis/batpuxadas/04/cpf.php?cpf={cpf}'  # Substitua pelo link correspondente

    if token in valid_tokens:
        try:
            response = requests.get(SOURCE_URL)
            
            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({'error': 'Falha ao obter dados do site'}), response.status_code
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'message': 'Token inválido!'}), 401

@app.route('/<string:token>/cpf5/<string:cpf>', methods=['GET'])
def get_cpf5(token, cpf):
    SOURCE_URL = f'https://x-search.xyz/test-by-x-slayer/apis/batpuxadas/05/cpf.php?cpf={cpf}'  # Substitua pelo link correspondente

    if token in valid_tokens:
        try:
            response = requests.get(SOURCE_URL)
            
            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({'error': 'Falha ao obter dados do site'}), response.status_code
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'message': 'Token inválido!'}), 401

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
