from flask import Flask, render_template



app = Flask (__name__)

@app.route('/')
def pagina_inicial():
    return "seja bem vindo"

@app.route('/usuario/<nome_usuario>')
def usuario(nome_usuario):
    return render_template('index (2).html' , nome_usuario=nome_usuario)

@app.route('/contatos')
def contatos():
    return render_template('index.html')


if __name__ =="__main__":
    app.run(debug=True)
