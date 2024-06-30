from flask import Flask, request
import sqlite3 # 追加

app_server = Flask(__name__)

@app_server.route('/')
def hello():
    return "Hello Minori"

@app_server.route('/getname')
def getname():
    return "Tori"
@app_server.route('/form')
def form():
    return render_template('index.html')

# 全体的に修正する
@app_server.route('/app', methods=['PUT'])
def app():
    if request.method != 'PUT':
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

    # name = request.form['name']
    # age = int(request.form['age'])
    # school = request.form['school']
    # comment = request.form['comment']
    
    
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    cur.execute("INSERT INTO user VALUES (?, ?, ?, ?)", (name, age, school, comment))

    con.commit()
    con.close()
    return "データが格納されました！"

if __name__ == "__main__":
    app_server.run(debug=True)

# main関数
if __name__ == "__main__":
    # サーバーが実際に立ち上がる
    # デバックオプションがTrueになっている
    app_server.run(debug=True)
    #

# if __name__ == "__main__":
#     app_server.run(debug=True)
#     from flask import Flask

# # Flaskクラスのインスタンスを立てる
# app_server = Flask(__name__)

# # '/'というURLの時に働くアクションを定義
# # @はデコレータといい、次の行で定義する関数やクラスに対しての処理に対して処理を行う
# @app_server.route('/')
# def hello():
#     # nameという変数に"Hello World"という文字を入れている
#     return "Hello World"



#curl --location --request GET 'http://127.0.0.1:5000/'
#
# from flask import Flask, request
# import sqlite3

# app_server = Flask(__name__) 
# #flaskのアプリを使ってflaskサーバーを立てている

# @app_server.route('/')
# #route：大元の画面、サーバーの一番最初のところ。ここからディレクトリ
# def hello():
#     return "Hello World"
# #hello wordlを返すようになっている

# @app_server.route('/getname')
# def getname():
#     return "Namiko"

# @app_server.route('/app', methods=['POST'])
# def app():
#     if request.method != 'POST':
#         return "Error", 405
#     return request.form['name']


    # if not 'name' in request.form:
    #     return "Name Key Error", 400
    # name = request.form['name']

    # if not 'age' in request.form:
    #     return "Age Key Error", 400
    # age = int(request.form['age'])

    # if not 'school' in request.form:
    #     return "School Key Error", 400
    # school = request.form['school']

    # if not 'comment' in request.form:
    #     return "Comment Key Error", 400
    # comment = request.form['comment']
    
    # con = sqlite3.connect('example.db')
    # cur = con.cursor()
    # cur.execute("INSERT INTO user VALUES (?, ?, ?, ?)", (name, age, school, comment))

    # con.commit()
    # con.close()
    # return "データが格納されました！"

    #aaa