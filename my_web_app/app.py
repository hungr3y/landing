from flask import Flask, render_template

PHRASE = "Welcome to my website!"
""" phrase to show in website"""
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', phrase=PHRASE)


if __name__ == '__main__':
    app.run(debug=True)
