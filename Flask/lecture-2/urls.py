from flask import Flask , redirect , url_for
import time
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the page</h1>"

# dynamic url
@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Hey, {name} Welcome to the page"
# redirection of a url
@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    time.sleep(1)
    return f"<h1>Congratz {sname} you passed with {marks}</h1>"
@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    time.sleep(1)
    return f"<h1>You Failed {sname} with {marks}</h1>"
@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        #redirect user to page fail + sending the path parameters too
        return redirect(url_for("failed",sname=name,marks =num))
    else:
        #redirect user to page pass
        return redirect(url_for("passed",sname=name,marks=num))

if __name__ == "__main__":
    app.run(debug=True)
