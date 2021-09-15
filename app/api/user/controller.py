from flask_jwt_extended import jwt_required
from flask_restx import Resource

from app.api.user.namespace import UserDoc
from app.api.user.service import UserService

api = UserDoc.api
data_resp = UserDoc.data_resp


@api.route("/<string:username>")
class UserGet(Resource):
    @api.doc(
        "Get a specific user",
        responses={
            200: ("User data successfully sent", data_resp),
            404: "User not found!",
        },
    )
    @jwt_required()
    def get(self, username):
        """ Get a specific user's data by their username """
        return UserService.get_user_data(username)
