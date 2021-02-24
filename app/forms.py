from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms import TextAreaField, PasswordField, TextField, IntegerField, SelectField
from wtforms.validators import DataRequired, InputRequired, Email
from wtforms.fields.html5 import EmailField


class Login(FlaskForm):
   Email = TextField('Email', validators = [InputRequired()])
   Password = PasswordField('Password', validators = [InputRequired()])


class ProfileForm(FlaskForm):
    F_Name = TextField('First Name', validators = [DataRequired()])
    L_Name = TextField('Last Name', validators = [DataRequired()])
    Email = EmailField('Email', validators = [DataRequired(), Email()], render_kw={"placeholder": "e.g. jdoe@example.com"})
    Password = PasswordField('Password', validators = [DataRequired()])

class Password(FlaskForm):
   Old = PasswordField('Password', validators = [DataRequired()])
   New = PasswordField('Password', validators = [DataRequired()])


class Form(FlaskForm):
   
   Name = TextField('Name', validators = [DataRequired()])
   Email = EmailField('Email', validators = [DataRequired(), Email()])
   Subject = TextField('Subject', validators = [DataRequired()])
   Message = TextAreaField('Message', validators = [DataRequired()])

class CareerForm(FlaskForm):
   Name = TextField('Name', validators = [DataRequired()])
   Email = EmailField('Email', validators = [DataRequired(), Email()])
   Cover = TextAreaField('Cover Letter', validators = [DataRequired()], render_kw={"placeholder": "Enter your cover letter here"})
   Resume = FileField('Resume', validators=[FileRequired(),FileAllowed(['doc','docx', 'pdf', 'Files only!'])]) 

   

class Report(FlaskForm):
   F_Name = TextField('First Name', validators = [DataRequired()])
   M_Name = TextField('Middle Name', validators = [DataRequired()]) 
   L_Name = TextField('Last Name', validators = [DataRequired()])
   Sex = SelectField('Gender', choices = [('Male', 'Male'),('Female', 'Female')])
   Age = IntegerField('Age', validators = [DataRequired()])
   Email = EmailField('Email', validators = [DataRequired(), Email()], render_kw={"placeholder": "e.g. jdoe@example.com"})
   Phone = TextField('Phone', validators = [DataRequired()])
   Illness = TextAreaField('Illness', validators = [DataRequired()])
   Comments = TextAreaField('Comments', validators = [DataRequired()])
   Prescription = TextAreaField('Prescription', validators = [DataRequired()])
   History = TextAreaField('History', validators = [DataRequired()])
   file = FileField('Subject Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
