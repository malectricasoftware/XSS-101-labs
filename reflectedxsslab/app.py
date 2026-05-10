#imports
from flask import Flask, render_template, request


app = Flask(__name__)



#return the payload
@app.route("/")
def index():
       return render_template("index.html")

@app.route("/name")
def name():
        return render_template("name.html",name=request.args.get("name"))

        
if __name__ == "__main__":
        app.run("0.0.0.0",5000)
