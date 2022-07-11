import json

from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

# Lista pré-cadastrada de desenvolvedores
desenvolvedores = [
 {
     'id': '0',
     'nome': 'Fernando',
     'habilidades':['Python', 'Flask']
     },
    {
     'id': '1',
     'nome': 'Ricardo',
     'habilidades':['Java', 'Spring']
     },
    {
     'id': '2',
     'nome': 'Haffner',
     'habilidades':['HTML', 'CSS']}
]


# Devolve um desenvolvedor através do ID (GET)
# Altera um desenvolvedor através do ID (PUT)
# Deleta um desenvolvedor através do ID (DELETE)
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe.'.format(id)
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados


    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído!'}

# Lista todos os desenvolvedores e permite registrar novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)