from flask import Flask, render_template, request

app = Flask(__name__)

##temp data
post1 = {
    "title": "Help with homework",
    "text": "i need help with this",
    "post_date": "04/18/23",
    "last_activity_date": "04/19/23",
    "image": None,
    "alt_text": None
}

post2 = {
    "title": "Cow",
    "text": "cool cow",
    "post_date": "04/18/23",
    "last_activity_date": "04/19/23",
    "image": "https://cdn.britannica.com/55/174255-050-526314B6/brown-Guernsey-cow.jpg",
    "alt_text": "cow"
}

posts = []
all_replies = []

posts.append(post1)
posts.append(post2)
for i in range(5):
   posts.append(post1)
   posts.append(post2)

post1reply = {
    "parent_id": 0, 
    "text": "look at this cow tho",
    "post_date": "04/19/23",
    "image": "https://cdn.britannica.com/55/174255-050-526314B6/brown-Guernsey-cow.jpg",
    "alt_text": "cow"
}

post1reply2 = {
    "parent_id": 0, 
    "text": "cool",
    "post_date": "04/19/23",
    "image": None,
    "alt_text": None
}

all_replies.append(post1reply)
all_replies.append(post1reply2)

def get_replies(post_id) -> list:
   replies = [reply for reply in all_replies if post_id == reply["parent_id"]]
   return replies
## end of temp data

@app.route('/')
def home():
    return render_template('home.html')

    if __name__ == '__main__':
     app.run(debug=True)

@app.get("/forum")
def forum_page():
    return render_template("forum.html", posts=enumerate(posts), total_posts=len(posts), total_replies=0)

@app.get("/post/<int:post_id>")
def get_post(post_id):
   post = posts[post_id]
   replies = get_replies(post_id)
   return render_template("post.html", post=post, replies=enumerate(replies))