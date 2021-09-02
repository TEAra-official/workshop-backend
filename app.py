from flask import Flask, render_template, request
app_server = Flask(__name__)

@app_server.route('/')
def hello():
    name = "Hello World"
    return name

@app_server.route('/getname')
def getname():
    name = "Namiko"
    return name

@app_server.route('/app', methods=['POST'])
def app():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = "no name."
    return name

if __name__ == "__main__":
    app_server.run(debug=True)