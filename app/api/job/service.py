from flask import current_app

from app.api.job.utils import load_data
from app.models.job import Job
from app.utils import err_resp, message, internal_err_resp


class JobService:
    @staticmethod
    def get_job_data(job_id):
        """ Get job data by job_id """
        if not (job := Job.query.filter_by(id=job_id).first()):
            return err_resp("Job ID not found!", "job_404", 404)

        try:
            job_data = load_data(job)

            resp = message(True, "Job data sent")
            resp["job"] = job_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
