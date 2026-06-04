from flask import Flask, render_template, request, redirect, session
from os import path
import lablib.posts
import lablib.users
import secrets

app = Flask(__name__)

app.secret_key=secrets.token_urlsafe(16)


@app.route("/",methods=["GET","POST"])
def index():
        if request.method == "GET":
                if request.args.get("failed"):
                        failed="failed"
                else:
                        failed=""
                return render_template("lab.html",failed=failed)       
        elif request.method=="POST":
                if lablib.users.login(request.form.get("name"),request.form.get("password")):
                        session["name"]=request.form.get("name")
                        return redirect("b")
                else:
                        return redirect("?failed=1")

@app.route("/register",methods=["POST"])
def register():
        lablib.users.create(request.form.get("name"),request.form.get("password"))
        return redirect("/")
                
@app.route("/name")
def name():
        return render_template("name2.html")

@app.route("/b")
def payload2():
        if "name" in session.keys():
                posts=lablib.posts.fetchall()
                if not posts:
                        posts=[]
                return render_template("posts.html",posts=posts)
        else:
                return redirect("/")

@app.route("/post",methods=["GET","POST"])
def post():
        if request.method == "POST":
                try:
                        lablib.posts.post(session["name"],request.form.get("content"))
                        return redirect("b")
                except Exception as E:
                        print(E)
                        return "fail"
        elif request.method == "GET":
                return render_template("post.html")
        
if __name__ == "__main__":
        app.run("0.0.0.0",5000)
