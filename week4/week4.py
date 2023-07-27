from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"

correct_account = "test"
correct_password = "test"

def validate_login(account, password):
    return account == correct_account and password == correct_password

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    account = request.form.get("test_account")
    password = request.form.get("test_password")
    if not account or not password: 
        empty_message = "請輸入帳號、密碼" 
        return redirect(url_for('error', message=empty_message))
    
    if validate_login(account, password):
        session['username'] = account
        return redirect(url_for('member'))
    else:
        error_message = "帳號、密碼輸入錯誤"
        if account == correct_account and password != correct_password:
            error_message = "密碼輸入錯誤"
        elif account != correct_account and password == correct_password:
            error_message = "帳號輸入錯誤"

        return redirect(url_for('error', message=error_message))

@app.route("/error")
def error():
    message = request.args.get('message', '帳號或密碼輸入錯誤')
    return render_template("error.html", message=message)

@app.route("/member")
def member():
    if 'username' in session:
        return render_template("member.html")
    else:
        return redirect(url_for('index'))

@app.route("/signout")
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=3000)
