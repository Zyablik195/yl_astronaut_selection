from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def a():
    return "Миссия Колонизация Марса"

@app.route('/promotion_image')
def index():
    items = ['Человечество вырастает из детства.',
             'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.',
             'И начнём с марса!',
    'Присоединяйся!']
    return render_template('base.html', items=items)

@app.route('/astronaut_selection')
def index1():
    items = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода, киберинженер, штурман, пилот дронов'.split(', ')
    return render_template('base1.html', items=items)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')