from flask import Flask, render_template, request

app = Flask(__name__)

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

posts.append(post1)
posts.append(post2)

@app.get("/forum")
def forum_page():
    return render_template("forum.html", posts=posts)