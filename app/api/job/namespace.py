from flask_restx import Namespace, fields


class JobDoc:
    api = Namespace("job", description="Job related operations using RabbitMQ broker.")
    job = api.model(
        "Job object",
        {
            "id": fields.Integer,
            "name": fields.String,
            "created": fields.DateTime,
        },
    )

    data_resp = api.model(
        "Job Data Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "job": fields.Nested(job),
        },
    )
