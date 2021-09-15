from flask import Blueprint
from flask_restx import Api

from app.api.user.controller import api as user_ns
from app.api.job.controller import api as job_ns

api_bp = Blueprint("api", __name__)

api = Api(
    api_bp,
    title="API (authorization required)",
    description="Main routes which work only with a valid authorization token.",
    authorizations={
        'JWT Token Authorization': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    security='JWT Token Authorization'
)

api.add_namespace(user_ns)
api.add_namespace(job_ns)
