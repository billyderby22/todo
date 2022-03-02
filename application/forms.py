from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField

class AddToDo(FlaskForm):
    title = StringField("Task Name")
    desc = StringField("task Description")
    status = SelectField("Status", choices=[('todo', 'todo'), ('done', 'done')])
    Proj_id = IntegerField
    Submit = SubmitField ("AddItem")

