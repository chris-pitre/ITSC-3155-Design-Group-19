from flask import Flask, abort, redirect, render_template, request, url_for, send_from_directory
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_bcrypt import Bcrypt
from re import fullmatch
from werkzeug.utils import secure_filename
import os

from src.repositories.post_repository import post_repository_singleton
from src.models import db, User
from datetime import datetime

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
login_manager = LoginManager()
bcrypt = Bcrypt()

app.secret_key = 'itsc3155secretkeyforwebsite'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '' #IMPORTANT!!! FILL IN YOUR OWN DATABASE HERE AND RUN ninerstudy-schema.sql TO CREATE TABLE 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
login_manager.session_protection = "strong"

db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)

@login_manager.user_loader
def load_user(user_email):
    return User.query.get(user_email)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/forum", methods=['GET', 'POST'])
def forum_page():
    posts = post_repository_singleton.get_posts()
    total_posts = post_repository_singleton.get_total_posts()
    total_replies = post_repository_singleton.get_total_replies()
    return render_template("forum.html", posts=posts, total_posts=total_posts, total_replies=total_replies, current_user=current_user)

@app.get("/post/<int:post_id>")
def get_post(post_id):
   post = post_repository_singleton.get_post_by_id(post_id)
   replies = post_repository_singleton.get_replies(post_id)
   return render_template("post.html", post=post, replies=replies, current_user=current_user)

@app.get('/about')
def about_page():
   return render_template("About.html")

@app.get('/login')
def login_page():
   return render_template("login.html")

@app.post('/login')
def log_in():
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    user = post_repository_singleton.get_user_from_email(email)
    if(user is None):
        return render_template("login.html", error="Invalid Email")
    if(bcrypt.check_password_hash(user.user_password, password)):
        login_user(user, remember=True)
        return redirect(url_for('forum_page'))
    else:
        return render_template("login.html", error="Invalid Password")

@app.get('/signup')
def signup_page():
   return render_template("signup.html")

@app.post('/signup')
def create_new_user():
    username = request.form.get('user', '')
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    if(not (fullmatch("^.+@uncc.edu", email) or fullmatch("^.+@charlotte.edu", email))):
        return render_template("signup.html", error="Not a UNCC email")
    if(post_repository_singleton.is_email_exists(email)):
        return render_template("signup.html", error="Email Already Exists")
    if(post_repository_singleton.is_username_exists(username)):
        return render_template("signup.html", error="Username Already Exists")
    if(len(password) < 8 or len(password) > 20):
        return render_template("signup.html", error="Unsuitable Password")
    password = bcrypt.generate_password_hash(password)
    new_user = post_repository_singleton.create_user(username, email, password)
    login_user(new_user, remember=True)
    return redirect(url_for('forum_page'))

@app.route('/signout')
@login_required
def sign_out():
    logout_user()
    return redirect(url_for('home'))

@app.get('/createPost')
@login_required
def create_post_page():
   return render_template("createPost.html")

@app.post('/createPost')
@login_required
def create_post():
    title = request.form.get('title', '')
    text = request.form.get('text', '')
    topic = request.form.get('topic_id', 'No Topic')
    user_id = current_user.user_id
    post_date = datetime.now()
    last_updated = post_date
    media_id = None
    if 'image' in request.files:
        image = request.files['image']
        if image and allowed_file(image.filename):
            print("help")
            filename = secure_filename(image.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(path)
            alttext = request.form.get('alttext', 'No Alt Text')
            new_media = post_repository_singleton.create_media(path, alttext)
            media_id = new_media.media_id
    if title == '' or text == '':
        abort(400)
    created_post = post_repository_singleton.create_post(title, text, topic, user_id, post_date, last_updated, media_id)
    return redirect(f'/post/{created_post.post_id}')

@app.get('/createReply/<int:post_id>')
@login_required
def create_reply_page(post_id):
    post = post_repository_singleton.get_post_by_id(post_id)
    return render_template("createReply.html", post=post)

@app.post('/createReply/<int:post_id>')
@login_required
def create_reply(post_id):
    user_id = current_user.user_id
    reply_text = request.form.get('text', '')
    media_id = None
    post_date = datetime.now()
    if 'image' in request.files:
        image = request.files['image']
        if image and allowed_file(image.filename):
            print("help")
            filename = secure_filename(image.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(path)
            alttext = request.form.get('alttext', 'No Alt Text')
            new_media = post_repository_singleton.create_media(path, alttext)
            media_id = new_media.media_id
    if reply_text == '':
        abort(400)
    created_reply = post_repository_singleton.create_reply(post_id, user_id, reply_text, media_id, post_date)
    return redirect(f'/post/{created_reply.post_id}')

@app.route('/uploads/<path:name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
     app.run(debug=True)