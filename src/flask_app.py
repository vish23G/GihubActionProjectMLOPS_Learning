from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
  return "Hello Word, This is Flask application!!"

if __name == "__main__":
  app.run(host="0.0.0.0",port=5000)

