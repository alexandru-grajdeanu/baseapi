from flask import Blueprint
from flask_restx import Api

from app.auth.controller import api as auth_ns

auth_bp = Blueprint("auth", __name__)

auth = Api(
    auth_bp,
    title="Authentication",
    description="Authenticate and receive tokens."
)
auth.add_namespace(auth_ns)
