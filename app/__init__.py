from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from flask_script import Manager
#from flask_migrate import Migrate, MigrateCommand
#from flask_login import LoginManager
# Config Values

UPLOAD_FOLDER = './app/static/uploads'

from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'passphare'
#app.config['MAIL_SERVER'] = 'smtp.gmail.com'
#app.config['MAIL_PORT'] = '2525' # (or try 2525,465)
#app.config['MAIL_USERNAME'] = 'videolover967@gmail.com'
#app.config['MAIL_PASSWORD'] = 'microsoft25'
#app.config['MAIL_USE_TLS'] = False
#app.config['MAIL_USE_SSL'] = True
#mail = Mail(app)
SECRET_KEY = 'Sup3r$3cretkey'

# Flask-Login login manager
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'login'
# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session





#app.config['SECRET_KEY'] = SECRET_KEY
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/project"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # added just to suppress a warning
#app.config.from_object(__name__)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)
#manager = Manager(app)
#manager.add_command('db', MigrateCommand)

app.config.from_object(__name__)
from app import views
