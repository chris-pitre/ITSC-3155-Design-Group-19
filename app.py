from flask import Flask, abort, redirect, render_template, request

from src.repositories.post_repository import post_repository_singleton
from src.models import db
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '' #IMPORTANT!!! FILL IN YOUR OWN DATABASE HERE AND RUN ninerstudy-schema.sql TO CREATE TABLE 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
     app.run(debug=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.get("/forum")
def forum_page():
    posts = post_repository_singleton.get_posts()
    return render_template("forum.html", posts=posts, total_posts=2, total_replies=0)

@app.get("/post/<int:post_id>")
def get_post(post_id):
   post = post_repository_singleton.get_post_by_id(post_id)
   replies = post_repository_singleton.get_replies(post_id)
   return render_template("post.html", post=post, replies=replies)

@app.get('/login')
def login_page():
   return render_template("login.html")

@app.get('/about')
def about_page():
   return render_template("About.html")

@app.get('/createPost')
def create_post_page():
   return render_template("createPost.html")

@app.post('/createPost')
def create_post():
    title = request.form.get('title', '')
    text = request.form.get('text', '')
    topic = request.form.get('topic_id', 'No Topic')
    user_id = 1 #replace when authentication exists
    post_date = datetime.now()
    last_updated = post_date
    media_id = None
    if title == '' or text == '':
        abort(400)
    created_post = post_repository_singleton.create_post(title, text, topic, user_id, post_date, last_updated, media_id)
    return redirect(f'/post/{created_post.post_id}')