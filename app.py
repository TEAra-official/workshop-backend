from flask import Flask, request
app_server = Flask(__name__)

@app_server.route('/')
def hello():
    return "Hello World"

@app_server.route('/getname')
def getname():
    return "Namiko"

@app_server.route('/app', methods=['POST'])
def app():
    if request.method != 'POST':
        return "no name."
    return request.form['name']

if __name__ == "__main__":
    app_server.run(debug=True)