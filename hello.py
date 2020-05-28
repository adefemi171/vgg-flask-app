from flask import Flask
from flask import make_response

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1 style='color:purple'>Testing this Flask App for VGG!</h1>"

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('Are you sure the %s exists?' %page_name, 404)
    return response

if __name__ == '__main__':
    app.run(port=8080)
