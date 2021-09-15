from flask_jwt_extended import jwt_required
from flask_restx import Resource

from app.api.job.namespace import JobDoc
from app.api.job.service import JobService

api = JobDoc.api
data_resp = JobDoc.data_resp


@api.route("/<string:job_id>")
class JobGet(Resource):
    @api.doc(
        "Get a specific job",
        responses={
            200: ("Job data successfully sent", data_resp),
            404: "Job not found!",
        },
    )
    @jwt_required()
    def get(self, job_id):
        """ Get a specific job's data by their job_id """
        return JobService.get_job_data(job_id)


@api.route("/")
class JobPost(Resource):
    @api.doc(
        "Create a job",
        responses={
            200: ("Job successfully created", data_resp),
            404: "Job not found!",
        },
    )
    @jwt_required()
    def post(self):
        pass
