from src.models import db, User, Media, Post, Reply
from sqlalchemy import desc

class PostRepository:

    def get_posts(self):
        all_posts = Post.query.order_by(desc(Post.post_date)).all()
        return all_posts
    
    def create_post(self, title, text, topic, user_id, date, last_updated, media_id):
        new_post = Post(title=title, post_text=text, topic=topic, user_id=user_id, post_date=date, last_updated=last_updated, media_id=media_id)
        db.session.add(new_post)
        db.session.commit()
        return new_post
    
    def get_post_by_id(self, post_id):
        post = Post.query.filter_by(post_id=post_id).first()
        return post
    
    def get_replies(self, post_id):
        replies = Reply.query.filter_by(post_id=post_id).order_by(desc(Reply.post_date)).all()
        return replies

#Repository Singleton
post_repository_singleton = PostRepository()