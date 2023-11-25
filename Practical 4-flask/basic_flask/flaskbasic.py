from flask import Flask
app=Flask(__name__)

@app.route("/Ak/<name>/<int:password>")
def display(name,password):
  return f"<h1>Name: {name}</h1> <h1>Password: {password}</h1>"

if __name__ == "__main__":
  app.run()