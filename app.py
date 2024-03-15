from flask import Flask, render_template as r, url_for, request, redirect

app = Flask(__name__)


@app.route("/")
def HelloWorld():
  return r("index.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
  if request.method == "POST":
    user = request.form['username']
    return redirect(url_for("user", usr=user))
  else:
    return r('login.html')

@app.route("/<usr>")
def user(usr):
  return f"hii, {usr}"

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
