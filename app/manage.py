from app import db
from app.models.post import Post


def create_posts():
    for i in range(20):
        post = Post(name="Post" + str(i), caption="Some long caption", image="https://source.unsplash.com/random/250x250")
        db.session.add(post)

    db.session.commit()

    return
