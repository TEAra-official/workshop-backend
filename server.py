from flask import Flask, request
import sqlite3

app_server = Flask(__name__)

@app_server.route('/')
def hello():
    return "Hello World"

@app_server.route('/getname')
def getname():
    return "Tori"

@app_server.route('/app', methods=['POST'])
def app():
    if request.method != 'POST':
        return "Error", 405

    if not 'name' in request.form:
        return "Name Key Error", 400
    name = request.form['name']

    if not 'age' in request.form:
        return "Age Key Error", 400
    age = int(request.form['age'])

    if not 'school' in request.form:
        return "School Key Error", 400
    school = request.form['school']

    if not 'comment' in request.form:
        return "Comment Key Error", 400
    comment = request.form['comment']
    
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    cur.execute("INSERT INTO user VALUES (?, ?, ?, ?)", (name, age, school, comment))

    con.commit()
    con.close()
    return "データが格納されました！"

if __name__ == "__main__":
    app_server.run(debug=True)
