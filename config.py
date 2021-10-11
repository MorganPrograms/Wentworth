from dotenv import load_dotenv
import os

load_dotenv()

CRSF_ENABLED = True
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda"
UPLOAD_FOLDER = "./app/static/uploads"
GET_FILE = "/static/uploads"
