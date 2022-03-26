from flask import Flask
from flask_basicauth import BasicAuth
from app.config import Config
from app.models import db, User, Thread


from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db, render_as_batch=True)
basic_auth = BasicAuth(app)
from app.admin import DashboardView
admin = Admin(app, index_view=DashboardView())
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Thread, db.session))



@app.before_first_request
def create_tables():
    db.create_all()


from app.views import *
