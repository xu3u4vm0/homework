from flask import Flask,render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")

def index():
	X = "<h1>資管二A 411146889 李易軒的求職相關資訊<br></h1>"
	X += "<a href=/about>我的個人簡介</a><br>"
	X += "<a href=/today>何倫碼測驗結果</a><br>"
	X += "<a href=/mis>MIS相關工作介紹</a><br>"
	X += "<a href=/welcome>求職履歷自傳</a><br>"
	return X




@app.route("/mis")
def mis():
	return render_template("account.html")

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html")

@app.route("/about")
def about():
    return render_template("1012.html")


@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("guest")
    return render_template("welcome.html", name=user)


if __name__ == "__main__":
	app.run()