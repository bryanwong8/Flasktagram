from app import db
from app.models.post import Post


def create_posts():
    for i in range(20):
        post = Post(name="Post" + str(i), image="https://source.unsplash.com/random/250x250")
        db.session.add(post)

    db.session.commit()

    return


def create_new_posts():
    for i in range(20):
        post = Post(name="Post" + str(i), caption="Some caption", image="https://source.unsplash.com/random/250x250")
        db.session.add(post)

    db.session.commit()

    return


def recreate_database():
    db.drop_all()
    db.create_all()

    return
