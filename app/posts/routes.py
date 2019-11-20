from flask import (render_template, url_for, flash, jsonify, redirect, Blueprint, request)
from app import db
from app.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=["GET", "POST"])
def post_new():
    form = PostForm()

    return render_template("viewsPosts/PostForm.html", form=form)
