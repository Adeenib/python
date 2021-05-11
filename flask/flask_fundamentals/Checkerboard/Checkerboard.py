from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def eight_by_eight(n=8, y=8):
    print(n)
    print(y)

    return render_template('Checkerboard.html', x=int(n), y=int(int(y)*0.5))


@app.route('/<n>/<y>')
def num_by_num(n=8, y=8):
    print(n)
    print(y)
    return render_template('Checkerboard.html', x=int(n), y=int(int(y)*0.5))


@app.route('/<n>/<y>/<color>/<color1>')
def num_by_color(n=8, y=8, color='red', color1='black'):
    print(n)
    print(y)
    print(color)
    print(color1)
    return render_template('Checkerboard.html', x=int(n), y=int(int(y)*0.5), color=color, color1=color1)


if __name__ == "__main__":
    app.run(debug=True)
