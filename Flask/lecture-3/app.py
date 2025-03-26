from flask import Flask , render_template , url_for , redirect
app = Flask(__name__)

#! decorator
@app.route("/") # endpoint
def home():
    return render_template("home.html",title="Home")
@app.route("/about")
def about():
    return render_template("about.html",title="About")
@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template("evaluate.html",number = num)
# start the app
if __name__ == "__main__":
    app.run(debug=True,port=8000)