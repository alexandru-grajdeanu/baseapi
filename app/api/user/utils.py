from app.models.schemas import UserSchema


def load_data(user_db_obj):
    user_schema = UserSchema()

    data = user_schema.dump(user_db_obj)

    return data
