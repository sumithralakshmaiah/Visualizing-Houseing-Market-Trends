from flask import Flask, render_template, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

