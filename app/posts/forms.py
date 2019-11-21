from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import FileField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    name = StringField("Name of Post", validators=[DataRequired()])
    caption = TextAreaField("Add a caption for your post!", validators=[DataRequired()])
    file = FileField('Cover Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'])
    ])
    submit = SubmitField("Submit")


class Delete(FlaskForm):
    delete = SubmitField("Delete")
