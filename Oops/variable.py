from flask import Flask
app=Flask(__name__)

@app.route("/Ak/<name>")
def prac(name):
  return "Hello there %s"%name

if __name__=="__main__":
  app.run()