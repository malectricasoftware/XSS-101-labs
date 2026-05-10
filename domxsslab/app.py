from flask import Flask, render_template


app = Flask(__name__)
                
@app.route("/")
def name():
        return render_template("index.html")

@app.route("/")
def name():
        return render_template("name.html")
        
if __name__ == "__main__":
        app.run("0.0.0.0",5000)
