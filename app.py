from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/forum")
def forum_page():
    return render_template("forum.html")