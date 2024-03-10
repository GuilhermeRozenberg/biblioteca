from flask import Flask , app, jsonify, request

app = Flask (__name__)

livros = [ 
   {
      'id': 1,
      'titulo': 'O Senhor dos Aneis - A Sociedade do Anel',
      'autor': 'J.R.R Tolkien',
   },
   {
      'id': 2,
      'titulo': 'Tron, O Legado',
      'autor': 'G. Sua Tia',
   },
   { 
      'id': 3,
      'titulo': 'Xmen - Evolution',
      'autor': 'P. Rereko',
   },
]
#
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)
#
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
#
@app.route('livros/<int:id>',methods=['PUT'])    
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#Criar
@app.route('/livros',methods=['POST'])
def inlcuir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)
 #Excluir 
@app.route('/livros/<int:id>',methods=['DELETE'])         
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros [indice]
            
app.run(port=5000,host='localhost',debug=True)
