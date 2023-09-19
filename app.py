from flask import Flask, render_template, request

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!<br>Vamos juntos aprender a programar.<br>Isso é apenas o começo!'

if __name__ == '__main__':
    app.run()

