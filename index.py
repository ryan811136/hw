from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    x ="作者:資管二A 黃于倫<br>"
    x +="<a href=/about>我的個人簡介</a><br>"
    x +="<a href=/account>MIS相關工作介紹</a><br>"
    x +="<a href=/today>職涯測驗結果</a><br>"
    x +="<a href=/welcome>未來規劃</a><br>"
    return x

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/today")
def today():
    return render_template("today.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


#if __name__ == "__main__":
    #app.run()
