from flask import Flask, render_template, request, redirect
from fp_module import fuerza, presion

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='YOMGUnidad2')


@app.route('/exec_fuerza', methods=['GET', 'POST'])
def execute() -> 'html':
    m = float(request.form['m'])
    a = float(request.form['a'])
    title = 'This is the fuerza\'s result'
    result = fuerza(m, a)
    return render_template('result.html',
                           the_title=title,
                           the_m=m,
                           the_a=a,
                           the_result=result, )


if __name__ == '__main__':
    app.run('localhost', 5002, debug=True)
