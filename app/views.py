"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
#from app import db
#from werkzeug.security import check_password_hash
#from flask_login import login_user, logout_user, current_user, login_required, login_manager,LoginManager
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from app.forms import Form, CareerForm
#from app import mail
from flask_mail import Message
#from app.models import Profile, Med_Reports 
import datetime


# Flask-Login login manager
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'login'

###
# Routing for your application.
###


@app.route('/', methods=['POST', 'GET'])
def Home():
    """Render the website's home page."""
    if request.method == 'GET':
        form = Form()
        return render_template('home.html', form = form )
    form = Form()
    if request.method == 'POST' and form.validate_on_submit():
        Name = form.Name.data
        Email = form.Email.data
        Subject = form.Subject.data
        message = form.Message.data
        f = open("Contact - "+Name+".txt","w+")
        f.write("Email Address: "+Email +"\n")
        f.write("Subject: "+Subject +"\n")
        f.write("Message: "+message)
        f.close()
        #subject = Subject
        #name = Name
        #email = Email
        #msg = Message(subject, sender="videolover967@gmail.com",recipients=["sirhcagrom@outlook.com"])
        #msg.body = Name+"\n+"+Email+"\n"+message
        #mail.send(msg)
        flash('Your message has been sent!', 'success')
        return redirect(url_for('Home'))
    return render_template('home.html', form = form)
@app.route('/About/')
def About():
    """Render the website's about page."""
    return render_template('about.html')
@app.route('/Services/')
def Services():
    """Render the website's services page."""
    return render_template('services.html')
@app.route('/Contact/', methods=['POST', 'GET'])
def Contact():
    """Render the website's contact page."""
    if request.method == 'GET':
        form = Form()
        return render_template('contact.html', form = form )
    form = Form()
    if request.method == 'POST' and form.validate_on_submit():
        Name = form.Name.data
        Email = form.Email.data
        Subject = form.Subject.data
        message = form.Message.data
        f = open("Contact - "+Name+".txt","w+")
        f.write("Email Address: "+Email +"\n")
        f.write("Subject: "+Subject +"\n")
        f.write("Message: "+message)
        f.close()
        #subject = Subject
        #name = Name
        #email = Email
        #msg = Message(Subject, sender=email,recipients=["sirhcnagrom@outlook.com"])
        #msg.body = message
        #mail.send(msg)
        flash('Your message has been sent!', 'success')
        return redirect(url_for('Home'))
    return render_template('contact.html', form = form)
@app.route('/External/')
def External():
    """Render the website's external page."""
    return render_template('external.html')
@app.route('/Staff/')
def Staff():
    """Render the website's Staff page."""
    return render_template('staff.html')
@app.route('/Careers/', methods = ['POST', 'GET'])
def Careers():
    """Render the website's careers page."""
    if request.method == 'GET':
        form = CareerForm()
        return render_template('careers.html', form = form )
    form = CareerForm()
    if request.method == 'POST' and form.validate_on_submit():
        Name = form.Name.data
        f = open("Applicant - "+Name+".txt","w+")
        Email = form.Email.data
        f.write(Email +"\n")
        Cover = form.Cover.data
        f.write(Cover)
        f.close()
        Resume = form.Resume.data
        filename = secure_filename(Resume.filename)
        Resume.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        flash('Your application has been sent!', 'success')
        return redirect(url_for('Home'))
    return render_template('careers.html', form = form )

@app.route('/Reports/')
def Reports():
    """Render the website's about page."""
    return render_template('Reports.html')



@app.route('/files/')
def files():
    if not session.get('logged_in'):
         abort(401)
    return render_template('files.html', file = get_uploaded_images())



@app.route('/Register', methods=['POST', 'GET'])
def Register():
    # Instantiate your form class
    if request.method == 'GET':
        form = ProfileForm()
        return render_template('Register.html', form = form)

    # Validate file upload on submit
    form = ProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Get file data and save to your uploads folder
        F_Name = form.F_Name.data
        L_Name =  form.L_Name.data
        Email = form.Email.data
        Password = form.Password.data
        profile = Profile(F_Name,L_Name,Email,Password)
        db.session.add(profile)
        db.session.commit()
        
        flash('Profile Added', 'success')
        return redirect(url_for('home'))
    return redirect(url_for('Register'))

@app.route('/profiles')
def profiles():
    profiles = Profile.query.all()
    return render_template('profiles.html', images = get_uploaded_images(), profiles = profiles)

@app.route('/profileuserid/<int:userid>')
def profileuserid(userid):
    profile = Profile.query.filter_by(id=userid).first()
    return render_template('profileuserid.html', profile = profile)
    

@app.route("/logout")
#@login_required
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))



# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session


'''
@app.route('/contact', methods = ['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        name = form.Name.data
        email = form.Email.data
        subject = form.Subject.data
        message = form.Message.data
        msg = Message(subject, sender=(name,email),recipients=[" 8ebd143712-1aa526@inbox.mailtrap.io"])
        flash('You have successfully filled out the form', 'success')
        msg.body = message
        mail.send(msg)
        return render_template('home.html')
    
    return render_template('contact.html', form = form)
'''

###
# The functions below should be applicable to all Flask apps.
###
#@login_manager.user_loader
def load_user(id):
    return Profile.query.get(int(id))
# Flash errors from the form if validation fails
def get_uploaded_images():
    rootdir = os.getcwd()
    print (rootdir)
    f = []
    for subdir, dirs, files in os.walk(rootdir + r'\app\static\uploads'):
        for file in files:
            f.append(file)
    return f[1:]
    
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
