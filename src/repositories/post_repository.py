from src.models import db, User, Media, Post, Reply
from sqlalchemy import desc, asc

class PostRepository:

    def is_username_exists(self, username):
        username = f'%{username}%'
        found_name = User.query.filter(User.user_username.like(username)).first() is not None
        return found_name
    
    def is_email_exists(self, email):
        email = f'%{email}%'
        found_email = User.query.filter(User.user_email.like(email)).first() is not None
        return found_email
    
    def create_user(self, username, email, password):
        new_user = User(user_username=username, user_email=email, user_password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    def get_user_from_email(self, email):
        email = f'%{email}%'
        user = User.query.filter(User.user_email.like(email)).first()
        return user

    def get_posts(self):
        all_posts = db.session.query(Post.post_id, Post.title, Post.topic, Post.post_text, Post.media_id, Post.post_date, Post.last_updated, User.user_username, Media.media_path, Media.media_alttext).\
            join(User, User.user_id == Post.user_id).\
            join(Media, Media.media_id == Post.media_id, isouter=True).order_by(desc(Post.last_updated)).all()
        return all_posts
    
    def get_total_posts(self):
        total_posts = Post.query.count()
        return total_posts

    def create_post(self, title, text, topic, user_id, date, last_updated, media_id):
        new_post = Post(title=title, post_text=text, topic=topic, user_id=user_id, post_date=date, last_updated=last_updated, media_id=media_id)
        db.session.add(new_post)
        db.session.commit()
        return new_post
    
    def get_post_by_id(self, post_id):
        post = db.session.query(Post.post_id, Post.title, Post.topic, Post.post_text, Post.media_id, Post.post_date, Post.last_updated, User.user_username, Media.media_path, Media.media_alttext).\
            filter_by(post_id=post_id).join(User, User.user_id == Post.user_id).\
            join(Media, Media.media_id == Post.media_id, isouter=True).order_by(desc(Post.last_updated)).first()
        return post
    
    def get_replies(self, post_id):
        replies = db.session.query(Reply.reply_text, Reply.media_id, Reply.post_date, User.user_username, Media.media_path, Media.media_alttext).\
            filter_by(post_id=post_id).join(User, User.user_id == Reply.user_id).\
            join(Media, Media.media_id == Reply.media_id, isouter=True).order_by(asc(Reply.post_date)).all()
        return replies
    
    def get_total_replies(self):
        total_replies = Reply.query.count()
        return total_replies

    def create_reply(self, post_id, user_id, reply_text, media_id, post_date):
        new_reply = Reply(post_id=post_id, user_id=user_id, reply_text=reply_text, media_id=media_id, post_date=post_date)
        db.session.add(new_reply)
        db.session.commit()
        original_post = Post.query.filter_by(post_id=post_id).first()
        original_post.last_updated = post_date
        db.session.commit()
        return new_reply
    
    def create_media(self, path, alttext):
        new_media = Media(media_path=path, media_alttext=alttext)
        db.session.add(new_media)
        db.session.commit()
        return new_media

#Repository Singleton
post_repository_singleton = PostRepository()