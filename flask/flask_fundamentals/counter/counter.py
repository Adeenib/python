from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 1
    elif 'count' in session:
        session['count'] = session['count'] + 1
    return render_template('counter.html', count=session['count'])


@app.route('/destroy_session')
def clean():
    if 'count' in session:
        session.clear()
    return render_template('counter.html')


if __name__ == "__main__":
    app.run(debug=True)
