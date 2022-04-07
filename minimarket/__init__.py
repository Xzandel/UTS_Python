from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = \
   'mysql+mysqlconnector://root:''@localhost/db_uts'
application.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# membuat objek dari kelas SQLAlchemy
db = SQLAlchemy(application)

from minimarket import routes
