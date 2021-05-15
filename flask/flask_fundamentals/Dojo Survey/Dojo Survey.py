from typing import Text
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def info():
    print(request.form)
    return render_template('info.html', name=request.form['name'],
                           location=request.form['loc'],
                           language=request.form['lang'],
                           comment=request.form['comment']
                           )


if __name__ == "__main__":
    app.run(debug=True)
