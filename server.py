from flask import Flask, render_template, request
import sqlite3

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
    if request.method != 'POST':
        return "Error"

    name = request.form['name']
    age = int(request.form['age'])
    school = request.form['school']
    comment = request.form['comment']
    
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    cur.execute("INSERT INTO user VALUES (?, ?, ?, ?)", (name, age, school, comment))

    con.commit()
    con.close()
    return "データが格納されました！"

if __name__ == "__main__":
    app_server.run(debug=True)