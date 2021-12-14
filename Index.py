from flask import Flask, render_template

app = Flask(__name__)
@app.route('/base')
def base():
    return render_template('base.html')
@app.route('/base2')
def base2():
    return render_template('base2.html')
@app.route('/')
def principal():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)