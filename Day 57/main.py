from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_posts = requests.get("https://api.npoint.io/d87c8f6badff1708a3a0", verify=False).json()
@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in blog_posts:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
