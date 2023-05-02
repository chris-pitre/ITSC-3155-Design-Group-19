from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_username = db.Column(db.String(50), nullable=False)
    user_password = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    posts = db.relationship("Post", backref="user")

class Media(db.Model):
    media_id = db.Column(db.Integer, primary_key=True, nullable=False)
    media_path = db.Column(db.String(1024), nullable=False)
    media_alttext = db.Column(db.String(512))
    posts = db.relationship("Post", backref="media")
    replies = db.relationship("Reply", backref="media")

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    topic = db.Column(db.String(255), nullable=False)
    post_text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    media_id = db.Column(db.Integer, db.ForeignKey("media.media_id"))
    post_date = db.Column(db.DateTime, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)
    replies = db.relationship("Reply", backref="post")

class Reply(db.Model):
    reply_id = db.Column(db.Integer, primary_key=True, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.post_id"), nullable=False)
    reply_text = db.Column(db.Text, nullable=False)
    media_id = db.Column(db.Integer, db.ForeignKey("media.media_id"))
    post_date = db.Column(db.DateTime, nullable=False)