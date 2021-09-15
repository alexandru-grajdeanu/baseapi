from app import ma


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = (
            "email",
            "name",
            "username",
            "joined_date",
            "role_id",
        )


class JobSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = (
            "id",
            "name",
            "created",
        )
