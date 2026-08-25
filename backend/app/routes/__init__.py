from flask import Blueprint

# Create blueprints
auth_bp = Blueprint('auth', __name__)
tickets_bp = Blueprint('tickets', __name__)
users_bp = Blueprint('users', __name__)

# Import routes to register them
from app.routes import auth, tickets, users
