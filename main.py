from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validador', methods=['POST'])
def validador():
    try:
        num = int(request.form['num'])
        if num >= 0:
            valor = 'positivo'
        else:
            valor = 'negativo'
        if num % 2 == 0:
            condicao = 'par'
        else:
            condicao = 'impar'
        return render_template('index.html', num=num, valor=valor, condicao=condicao)
    except ValueError as e:
        return render_template('erro.html', mensagem=f"Entrada inválida: {e}")
    finally:
        print("obrigado por usar o programa ")


if __name__ == '__main__':
    app.run(debug=True)