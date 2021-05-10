from flask import Flask, render_template
app = Flask(__name__)


@app.route("/play")
def play():

    return render_template('index.html', id=3)


@app.route("/play/<id>")
def namesbyid(id,):

    print(id)
    return render_template('index.html',  id=int(id))


@ app.route("/play/<id>/<color>")
def color(id, color):
    print(color)
    print(id)
    return render_template('index.html',  id=int(id), color=color)


if __name__ == "__main__":
    app.run(debug=True)
