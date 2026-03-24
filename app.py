from flask import Flask,render_template,request,redirect,url_for
import sqlite3
app=Flask(__name__)
def init_db():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   email TEXT,
                   age INTEGER)
                   ''')
    conn.commit()
    conn.close()
@app.route('/')
def home():
    conn=sqlite3.connect('database.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users")
    users=cursor.fetchall()
    conn.close()
    return render_template('index.html',users=users)
@app.route('/add',methods=['POST'])
def add_user():
    name=request.form.get('name')
    email=request.form.get('email')
    age=request.form.get('age')
    conn=sqlite3.connect('database.db')
    cursor=conn.cursor()
    cursor.execute("INSERT INTO users(name,email,age) VALUES (?,?,?)",(name,email,age))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))
if __name__=="__main__":
    init_db()
    app.run(debug='True')