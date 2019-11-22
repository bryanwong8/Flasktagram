from flask import (render_template, url_for, flash, redirect, Blueprint, request)
from app import db
from app.models.post import Post
from app.posts.forms import Delete, PostForm
from app.posts.utils import add_image

posts = Blueprint('posts', __name__)


# Route for the homepage
@posts.route("/")
def post_home():
    post_list = Post.query.all()
    form = Delete()

    return render_template("viewsPosts/PostHome.html", posts=post_list, form=form)


# Route to create a new post
@posts.route("/posts/new", methods=["GET", "POST"])
def post_new():
    form = PostForm()

    if form.validate_on_submit():
        image = add_image(form.file.data, "labs")
        post = Post(name=form.name.data, caption=form.caption.data, image=image)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for("posts.post_home"))
    return render_template("viewsPosts/PostForm.html", form=form, title="Create A Post")


# Route to edit a post
@posts.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
def post_edit(post_id):
    form = PostForm()
    post = Post.query.get(post_id)

    if form.validate_on_submit():
        new_image = add_image(form.file.data, "labs")
        post.name = form.name.data
        post.caption = form.caption.data
        post.image = new_image
        db.session.commit()
        return redirect(url_for("posts.post_home"))
    elif request.method == "GET":
        form.name.data = post.name
        form.caption.data = post.caption
        form.file.data = post.image
    return render_template("viewsPosts/PostForm.html", form=form)


# Route to delete a post
@posts.route("/posts/<int:post_id>/delete", methods=["POST"])
def post_delete(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("posts.post_home"))
