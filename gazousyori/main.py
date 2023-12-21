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
def gazousyori1():
    return render_template('gazousyori2.html')

@app.route('/gazousyori3')
def gazousyori1():
    return render_template('gazousyori3.html')


if __name__ == '__main__':
    app.run(debug=True)
