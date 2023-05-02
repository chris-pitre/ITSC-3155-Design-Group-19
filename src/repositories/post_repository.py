from src.models import db, User, Media, Post, Reply
from sqlalchemy import desc, asc

class PostRepository:

    def get_posts(self):
        all_posts = Post.query.order_by(desc(Post.last_updated)).all()
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
        post = Post.query.filter_by(post_id=post_id).first()
        return post
    
    def get_replies(self, post_id):
        replies = Reply.query.filter_by(post_id=post_id).order_by(asc(Reply.post_date)).all()
        return replies
    
    def get_total_replies(self):
        total_replies = Reply.query.count()
        return total_replies

    def create_reply(self, post_id, user_id, reply_text, media_id, post_date):
        new_reply = Reply(post_id=post_id, user_id=user_id, reply_text=reply_text, media_id=media_id, post_date=post_date)
        db.session.add(new_reply)
        db.session.commit()
        original_post = post_repository_singleton.get_post_by_id(post_id)
        original_post.last_updated = post_date
        db.session.commit()
        return new_reply

#Repository Singleton
post_repository_singleton = PostRepository()