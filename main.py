from flask import Flask, redirect, render_template, jsonify
import os
import requests

app = Flask(__name__)

valid_tokens = ["zealmeida"]

@app.route('/cpf1/<string:cpf>', methods=['GET'])
def get_cpf1(cpf):
    SOURCE_URL = f'https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/01/cpf.php?cpf={cpf}' 

    try:
        response = requests.get(SOURCE_URL)

        
        if response.status_code == 200:
           

            if response.json()['status'] == 1:

                dados = response.json()['dados']

                cpf = dados[0].get('CPF', 'Nao consta')
                nome = dados[0].get('Nome', 'Nao consta')
                mae = dados[0].get('Nome_Mae', 'Nao consta')
                nasc = dados[0].get('Data_Nascimento', 'Nao consta')
                sexo = dados[0].get('Sexo', 'Nao consta')


                if nasc != 'Nao consta':
                    from datetime import datetime
                    try:
                        nasc_obj = datetime.strptime(nasc, "%Y-%m-%d")  
                        nasc = nasc_obj.strftime("%d/%m/%Y") 
                    except ValueError:
                        nasc = "Formato de data inválido"


                final = { 
                    "dados" : [ {
                    "cpf": cpf,
                    "nome": nome,
                    "mae": mae,
                    "nasc": nasc,
                    "sexo": sexo
                     }],
                    "status": "sucesso"
                }


                
                return jsonify(final), 200
            
            else:
                return jsonify({'status' : 'Nao consta'}), response.status_code

        else:
            return jsonify({'status': 'erro hospedagem'}), response.status_code
    except Exception as e:
        return jsonify({'status': 'erro banco'}), 500
    

@app.route('/cpf2/<string:cpf>', methods=['GET'])
def get_cpf2(cpf):
    SOURCE_URL = f'https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/02/cpf.php?cpf={cpf}'  # Substitua pelo link correspondente


    try:
        response = requests.get(SOURCE_URL)
        
        if response.status_code == 200:
           

            if response.json()['status'] == 'success':

                dados = response.json()['data']

                cpf = dados[0].get('CPF', 'Nao consta')
                nome = dados[0].get('Nome', 'Nao consta')
                mae = dados[0].get('Nome_Mae', 'Nao consta')
                nasc = dados[0].get('Data_Nascimento', 'Nao consta')
                sexo = dados[0].get('Sexo', 'Nao consta')

                final = { 
                    "dados" : [ {
                    "cpf": cpf,
                    "nome": nome,
                    "mae": mae,
                    "nasc": nasc,
                    "sexo": sexo
                     }],
                    "status": "sucesso"
                }
                
                return jsonify(final), 200
            
            else:
                return jsonify({'status' : 'Nao consta'}), response.status_code
            
        else:

            return jsonify({'status': 'erro hospedagem'}), response.status_code
        
    except Exception as e:
        return jsonify({'status': 'erro banco'}), 500    


@app.route('/cpf3/<string:cpf>', methods=['GET'])
def get_cpf3(cpf):
    SOURCE_URL = f'https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/03/cpf.php?cpf={cpf}'
    try:
        response = requests.get(SOURCE_URL)

                
        if response.status_code == 200:
       

            if 'CPF' in response.json()[0] :

                dados = response.json()[0]

                cpf = dados.get('CPF', 'Nao consta')
                nome = dados.get('Nome', 'Nao consta')
                mae = dados.get('Nome_Mae', 'Nao consta')
                nasc = dados.get('Data_Nascimento', 'Nao consta')
                sexo = dados.get('Sexo', 'Nao consta')

                final = { 
                    "dados" : [ {
                    "cpf": cpf,
                    "nome": nome,
                    "mae": mae,
                    "nasc": nasc,
                    "sexo": sexo[0]
                     }],
                    "status": "sucesso"
                }
                
                return jsonify(final), 200
            
            else:
                return jsonify({'status' : 'Nao consta'}), response.status_code
            
        else:

            return jsonify({'status': 'erro hospedagem'}), response.status_code
        
    except Exception as e:
        return jsonify({'status' : 'Nao consta'}), 500 


@app.route('/cpf4/<string:cpf>', methods=['GET'])
def get_cpf4(cpf):
    SOURCE_URL = f'https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/04/cpf.php?cpf={cpf}'  # Substitua pelo link correspondente


    try:
        response = requests.get(SOURCE_URL)

        
        if response.status_code == 200:


            if 'dados' in response.json()[0]['response']:


                dados = response.json()[0]['response']

                cpf = dados['dados']['CONTATOS'].get('CPF', 'Nao consta')
                nome = dados['dados']['CONTATOS'].get('NOME', 'Nao consta')
                mae = dados['dados']['CONTATOS'].get('NOME_MAE', 'Nao consta')
                nasc = dados['dados']['CONTATOS'].get('NASC', 'Nao consta')
                sexo = dados['dados']['CONTATOS'].get('SEXO', 'Nao consta')

                if nasc != 'Nao consta':
                    from datetime import datetime
                    try:
                        
                        nasc_obj = datetime.strptime(nasc, "%Y-%m-%d %H:%M:%S.%f") 
                        nasc = nasc_obj.strftime("%d/%m/%Y") 
                    except ValueError:
                        nasc = "Formato de data inválido"


                final = { 
                    "dados" : [ {
                    "cpf": cpf,
                    "nome": nome,
                    "mae": mae,
                    "nasc": nasc,
                    "sexo": sexo
                     }],
                    "status": "sucesso"
                }


                
                return jsonify(final), 200
            
            else:
                return jsonify({'status' : 'Nao consta'}), response.status_code
        else:
            return jsonify({'status': 'erro hospedagem'}), response.status_code
        
    except Exception as e:
        return jsonify({'status': 'erro banco'}), 500 


@app.route('/cpf5/<string:cpf>', methods=['GET'])
def get_cpf5(cpf):
    SOURCE_URL = f'https://x-search.xyz/3nd-p01n75/xsiayer0-0t/batpuxadas260125/r0070x/05/cpf.php?cpf={cpf}'  # Substitua pelo link correspondente

    try:
        response = requests.get(SOURCE_URL)
        
        if response.status_code == 200:
           

            if response.json()['status'] == 1:

                dados = response.json()['dados']

                cpf = dados[0].get('CPF', 'Nao consta')
                nome = dados[0].get('Nome', 'Nao consta')
                mae = dados[0].get('Nome_Mae', 'Nao consta')
                nasc = dados[0].get('Data_Nascimento', 'Nao consta')
                sexo = dados[0].get('Sexo', 'Nao consta')

                final = { 
                    "dados" : [ {
                    "cpf": cpf,
                    "nome": nome,
                    "mae": mae,
                    "nasc": nasc,
                    "sexo": sexo
                     }],
                    "status": "sucesso"
                }


                
                return jsonify(final), 200
            
            else:
                return jsonify({'status' : 'Nao consta'}), response.status_code
        else:
            return jsonify({'status': 'erro hospedagem'}), response.status_code
        
    except Exception as e:
        return jsonify({'status': 'erro banco'}), 500 

    
@app.route('/cpf7/<string:cpf>', methods=['GET'])
def get_cpf7(cpf):
    SOURCE_URL = f'https://api.bronxservices.net/consulta/YWt5YmlzY2ZhcmRzOm11ZGFyMTIz/srs22/cpf/{cpf}'  # Substitua pelo link correspondente

    try:
        response = requests.get(SOURCE_URL)

                
        if response.status_code == 200:
       

            if 'dados' in response.json():

                dados = response.json()['dados']

                cpf = dados.get('CPF', 'Nao consta')
                nome = dados.get('NOME', 'Nao consta')
                mae = dados.get('NOME_MAE', 'Nao consta')
                nasc = dados.get('NASC', 'Nao consta')
                sexo = dados.get('SEXO', 'Nao consta')


                if nasc != 'Nao consta':
                    from datetime import datetime
                    try:
                        # Verifica o formato da data fornecida
                        nasc_obj = datetime.strptime(nasc, "%Y-%m-%d %H:%M:%S.%f")  # Formato com milissegundos
                        nasc = nasc_obj.strftime("%d/%m/%Y")  # Converte para o formato desejado
                    except ValueError:
                        nasc = "Formato de data inválido" 




                final = { 
                    "dados" : [ {
                    "cpf": cpf,
                    "nome": nome,
                    "mae": mae,
                    "nasc": nasc,
                    "sexo": sexo
                     }],
                    "status": "sucesso"
                }
                
                return jsonify(final), 200
            
            else:
                return jsonify({'status' : 'Nao consta'}), response.status_code
            
        else:

            return jsonify({'status': 'erro hospedagem'}), response.status_code
        
    except Exception as e:
        return jsonify({'status' : 'Nao consta'}), 500 
    

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
