from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route("/dojo/<name>")
def names(name):
    print(name)
    return "Hi "+name


@app.route("/dojo/<name>/<id>")
def namesbyid(name, id):
    print(name)
    print(id)
    return (name+" ")*int(id)


if __name__ == "__main__":
    app.run(debug=True)
