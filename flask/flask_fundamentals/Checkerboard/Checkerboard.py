from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def eight_by_eight(n=8, y=8):
    print(n)
    print(y)

    return render_template('Checkerboard.html', x=int(n), y=int(int(y)*0.5))


@app.route('/<n>/<y>')
@app.route('/<n>/<y>/<color>/<color1>')
def num_by_color(n=8, y=8, color='red', color1='black'):
    import math
    print(n)
    print(y)
    print(color)
    print(color1)
    size = int(y)*50

    return render_template('Checkerboard.html', x=int(n), y=math.ceil(int(y)*0.5), color=color, color1=color1, fm=int(y), size=size)


if __name__ == "__main__":
    app.run(debug=True)
