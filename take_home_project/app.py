from flask import Flask
import os
app.debug = True


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    port = 8888
    app.run(host='0.0.0.0', port=port)
