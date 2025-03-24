from flask import Flask
app = Flask(__name__)

#! decorator
@app.route("/") # endpoint
def home():
    return "<h1>Welcome to the Home Page!<h1>"
@app.route("/about")
def about():
    return "<h1>Welcome to the about Page!</h1>"
# path parameter
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hi ,{name.title()},you'r welcome</h1>"
@app.route("/addition/<int:num>")
def addition(num):
    return f"<h1>input is {num} output is {num+10}</h1>"
# multiple path parameter
@app.route("/addition_two/<int:num1>/<int:num2>")
def addition_two(num1,num2):
    return f"<h1>{num1}+{num2} is {num1+num2}"

# start the app
if __name__ == "__main__":
    app.run(debug=True)