from flask import Flask, redirect, render_template, jsonify
import os
import requests

app = Flask(__name__)

valid_tokens = os.environ.get('TOKENS')

@app.route('/<string:token>/cpf1/<string:cpf>', methods=['GET'])
def get_cpf1(token, cpf):
    SOURCE_URL = f'https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/01/cpf.php?cpf={cpf}'  # Substitua pela URL real

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
    SOURCE_URL = f'https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/02/cpf.php?cpf={cpf}'  # Substitua pelo link correspondente

    if token in valid_tokens:
        try:
            response = requests.get(SOURCE_URL)
            
            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({"status":"error"}), response.status_code
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'message': 'Token inválido!'}), 401

@app.route('/<string:token>/cpf3/<string:cpf>', methods=['GET'])
def get_cpf3(token, cpf):
    SOURCE_URL = f'https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/03/cpf.php?cpf={cpf}'
    SECOND_API_BASE_URL = "https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/01/nome.php?nome="

    
    if token in valid_tokens:
        try:
            # Faz a primeira solicitação GET para obter o nome
            response = requests.get(SOURCE_URL)
            
            if response.status_code == 200:
                # A resposta já é uma lista, então não precisamos usar .json()
                dados_cpf = response.json()
                # Verifica se há dados na lista e retorna o nome
                
                print(SOURCE_URL)
                if dados_cpf and "Nome" in dados_cpf[0]:
                    nome_completo = dados_cpf[0].get("Nome", "Nome não encontrado")
                    if nome_completo == "Nome não encontrado":
                        return jsonify({"status":"error"}), 404
                    
                    
                    # Faz uma segunda requisição para a API usando o final do nome
                    second_api_url = f"{SECOND_API_BASE_URL}{nome_completo}"
                    second_response = requests.get(second_api_url)
                    
                    if second_response.status_code == 200:
                        # Retorna o resultado da segunda API
                        return jsonify(second_response.json()), 200
                    else:
                        return jsonify({"status":"error"}), second_response.status_code
                else:
                    return jsonify({"status":"error"}), 404
            else:
                return jsonify({"status":"error"}), response.status_code
        except Exception as e:
            return jsonify({"status":"error"}), 500
    else:
        return jsonify({'message': 'Token inválido!'}), 401

@app.route('/<string:token>/cpf4/<string:cpf>', methods=['GET'])
def get_cpf4(token, cpf):
    SOURCE_URL = f'https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/04/cpf.php?cpf={cpf}'  # Substitua pelo link correspondente

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
    SOURCE_URL = f'https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/05/cpf.php?cpf={cpf}'  # Substitua pelo link correspondente

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
    
@app.route('/<string:token>/cpf7/<string:cpf>', methods=['GET'])
def get_cpf7(token, cpf):
    SOURCE_URL = f'https://api.bronxservices.net/consulta/YWt5YmlzY2ZhcmRzOm11ZGFyMTIz/srs22/cpf/{cpf}'  # Substitua pelo link correspondente

    if token in valid_tokens:
        try:
            response = requests.get(SOURCE_URL)
            
            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({"status":"error"}), response.status_code
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({"status":"error"}), 401
    
@app.route('/<string:token>/nome/<string:nome>', methods=['GET'])
def get_nome(token, nome):
    SOURCE_URL = f'https://api.bronxservices.net/consulta/YWt5YmlzY2ZhcmRzOm11ZGFyMTIz/basica/nome/{nome}'  # Substitua pelo link correspondente

    if token in valid_tokens:
        try:
            response = requests.get(SOURCE_URL)
            
            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({"status":"error"}), response.status_code
        except Exception as e:
            return jsonify({"status":"error"}), 500
    else:
        return jsonify({"status":"error"}), 401

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
