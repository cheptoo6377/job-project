from flask_restful import Api
from flask import Flask, jsonify, redirect, request, url_for
from flask_security import SQLAlchemyUserDatastore, Security, current_user
from flask_security.signals import user_registered

from config import Config
from app.extension import db, csrf
from app.forms.register import CustomRegistrationForm
from app.models import RoleModel, UserModel, JobModel
from app.resources.user import Users, Userr
from app.resources.job import Jobs, Job
from app.routes import main as main_blueprint, mail



# --- Initialize Flask app ---
app = Flask(__name__)
app.config.from_object(Config)
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'your_key'

# --- Initialize extensions ---
csrf.init_app(app)
db.init_app(app)
mail.init_app(app)

# --- Setup Flask-Security ---
user_datastore = SQLAlchemyUserDatastore(db, UserModel, RoleModel)
security = Security(app, user_datastore, register_form=CustomRegistrationForm)

# --- Register API and blueprints ---
api = Api(app)
app.register_blueprint(main_blueprint)

# --- Create database tables ---
with app.app_context():
    db.create_all()

# --- Register signal handlers ---
@user_registered.connect_via(app)
def user_registered_sighandler(sender, user, confirm_token, **extra):
    """Handle post-registration logic"""
    default_role = RoleModel.query.filter_by(name='applicant').first()
    
    if default_role and not user.roles:
        user.roles.append(default_role)
        db.session.commit()

    print(f"New user registered: {user.email} with roles: {[role.name for role in user.roles]}")

 
# --- Register API resources ---
api.add_resource(Users, '/api/users')
api.add_resource(Userr, '/api/users/<int:id>')
api.add_resource(Jobs, '/api/jobs')
api.add_resource(Job, '/api/jobs/<int:id>')
# Redirect authenticated users away from /login and /register
@app.before_request
def _block_auth_from_auth_views():
    if request.endpoint in {"security.login", "security.register"} and current_user.is_authenticated:
        return redirect(url_for("security.post_login"))
