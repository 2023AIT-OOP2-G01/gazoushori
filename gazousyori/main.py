from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    input = request.form.get('name')


    return render_template('index.html')

@app.route('/gazousyori1')
def gazousyori1():
    return render_template('gazousyori1.html')

@app.route('/gazousyori2')
def gazousyori2():
    return render_template('gazousyori2.html')

@app.route('/gazousyori3')
def gazousyori3():
    return render_template('gazousyori3.html')

@app.route('/gazousyori4')
def gazousyori4():
    return render_template('gazousyori4.html')

@app.route('/gazousyori5')
def gazousyori5():
    return render_template('gazousyori5.html')


if __name__ == '__main__':
    app.run(debug=True)