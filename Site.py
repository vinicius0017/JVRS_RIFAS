from flask import Flask, render_template



app = Flask (__name__)

@app.route('/')
def pagina_inicial():
    return "seja bem vindo"





if __name__ =="__main__":
    app.run(debug=True)
