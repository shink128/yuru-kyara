# Flaskを使えるようにする
from flask import Flask,request,redirect,session
from flask import render_template
import random,sqlite3

# appという名前でFlaskアプリを作る
app = Flask(__name__)
app.secret_key ="sunabaco"
# Flaskを使ったページ
# /にアクセスしたときの指示
@app.route("/")
# hello_world()関数を実行
def hello_world():
    return "<p>Hello, World!</p>"

#/foodページにアクセスすると食べ物の名前がかえってkる
@app.route("/food")
def food():
    return "モスバーガー"

#htmlを用いて表示
#/hello ページにアクセスしたときの表示
@app.route("/serch")
def serch():
    return render_template("serch.html",user_name = "shink")

@app.route("/sports")
def sports():
    py_sports = "football"
    return render_template("hello.html",html_sports = py_sports)

# 天気予報もどき
# /weatherページにアクセスすると
# weather関数が実行
# 1 明日は晴れです　２weather.htmlを使って「明日は晴れです」と表示
# 3 weather.htmlを使って「明日は００です」と表示　
# 4 天気をランダムに　　神　実際の天気

# 問１
# @app.route("/weather")
# def weather():
#     return "<p>明日は晴れです</p>"


# 問２
# @app.route("/weather")
# def weather():
#     return render_template("weather.html")

# 問3
# @app.route("/weather")
# def weather():
#     return render_template("weather.html",next_weather ="晴れのち曇り")

# 問４



#おみくじアプリ

# 「大吉です」とgacha.html を使って表示させる

@app.route("/gacha")
def gacha():
    # /gacha にアクセスすると　gachaという関数が実行される  
    # l = ["大吉", "中吉", "小吉", "末吉","凶"]
    # return render_template("gacha.html",gacha =random.choice(l))

    omikuji = ["大吉である！", "小吉です","凶だ"]
    omikuji_python = random.choice(omikuji)
    # print(omikuji_python)
    return render_template("gacha.html",gacha = omikuji_python)

# DBに接続して情報を取得
# /listにアクセスするとDBに接続して情報を取得してプリント
# @app.route("/list")
# def task_list():
#     # SQlを使えるようにするモジュール
#     import sqlite3
#     # DBに接続
#     conn = sqlite3.connect("task_list.db")
#     # データを操作できるようにする
#     c=conn.cursor()
#     # SQL文　データの取得
#     c.execute("select * from task")
#     # データの受け取り
#     task = c.fetchall()
#     # DBとの接続終了
#     c.close()
#     print(task)

#     return render_template("list.html", task = task)
#     # 情報を取得してプリント

@app.route("/add")
def add2():
    return render_template("add.html")





    # Dbに値を追加
@app.route("/add" ,methods=["post"])
def add():
    
    
    py_task = request.form.get("input_task")
    
    conn = sqlite3.connect("task_list.db")
        # カーソルの作成
    c= conn.cursor()
    

        # SQL
    c.execute("INSERT INTO task values(null,?)",(py_task,))

        # 変更を書き込む
    conn.commit()
        #DBとの接続終了
    c.close()

    return redirect("/")

# エラーの表示（４０４エラー）
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404    

@app.route("/list")
def list():
    # DB接続
    conn = sqlite3.connect('task_list.db')
    #DBを操作できるようにする
    c = conn.cursor()
    #idとtaskをテーブルからとってくるSQL文
    c.execute("SELECT id,task FROM task")
    # 結果を配列に格納（辞書型）
    # 空の配列をいったん作る
    task_list_py = []
    # DBから取得した情報の数(行=row）だけ繰り返して辞書型に格納
    for row in c.fetchall():
        # 行（row）配列の[0]個目はid,[1]個目はtaskと名前を付ける
        task_list_py.append({"id":row[0],"task":row[1]})
    #DBとの接続を終了
    c.close()
    return render_template("list.html",task = task_list_py)

# 編集のルート
@app.route('/update/<id>')
def update(id):
    # update.html　を表示　ID　タスク内容を渡す
    conn = sqlite3.connect('task_list.db')
    c = conn.cursor()
    c.execute("SELECT task FROM task where id = ?",(id,))
    py_task = c.fetchone()
    conn.close()

    return render_template('update.html',id =id,task = py_task)



@app.route("/update/<id>",methods=["post"])
def update_post(id):
    
    import sqlite3
    py_task = request.form.get("input_task")
    
    conn = sqlite3.connect("task_list.db")
        # カーソルの作成
    c= conn.cursor()
    

        # SQL
    c.execute("UPDATE task SET task = ? WHERE id =?",(py_task,id))

        # 変更を書き込む
    conn.commit()
        #DBとの接続終了
    c.close()

    return redirect("/list")

@app.route('/delete/<id>')
def delete(id):
    # update.html　を表示　ID　タスク内容を渡す
    conn = sqlite3.connect('task_list.db')
    c = conn.cursor()
    c.execute("DELETE FROM task  WHERE id =?",(id,))
    conn.commit()
    conn.close()

    return redirect("/list")


@app.route("/signup")
def signup():
    return render_template("signup.html")
 
# signup.htmlで登録が押されたときにデータをDBに送信する
@app.route("/signup",methods=["post"])
def signup_post():  

# フォームのinput_nameとinput_passwordに入力されたデータを取得

    py_name = request.form.get("input_name")
    py_pass = request.form.get("input_password")

    
    # DBと接続
    conn = sqlite3.connect("task_list.db")
    #    データを操作できるようにする
      
    c= conn.cursor()
    
    # データの処理（SQL文）
    c.execute("INSERT INTO user values(null,?,?)",(py_name,py_pass))

        # 変更を書き込む
    conn.commit()
        #DBとの接続終了
    c.close()

    return redirect("/signin")

@app.route("/signin")
def signin():
    return render_template("signin.html")
 # signup.htmlで登録が押されたときにデータをDBに送信する
@app.route("/signin",methods=["post"])
def signin_post():  
    py_name = request.form.get("input_name")
    py_pass = request.form.get("input_password")
    conn = sqlite3.connect("task_list.db")
    c= conn.cursor()
    # データの処理（SQL文：py_name　と　py_pass が一致するIDを取得
    c.execute("select id from user WHERE user_name =? and password = ?",(py_name,py_pass))
    
    # ユーザーの箱にセレクトしてきたIDをいれる
    user = c.fetchone()

        #DBとの接続終了
    c.close()

    # 一致するユーザーがいなかったらサインインのページに
    if user is None :
        return render_template("signin.html")
    # ユーザーがいた場合　LISTページに, 
    else:
        session["id"]=user[0]
        return redirect("/list")

# サインアウト機能
@app.route("/signout")
def signout():
    session.pop("id,None")
    session.clear()
    return redirect("/signin")


# サーバーを立ち上げる
if __name__== '__main__':
    app.run(debug=True)

