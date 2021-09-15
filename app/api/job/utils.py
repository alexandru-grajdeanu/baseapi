from app.models.schemas import JobSchema


def load_data(job_db_obj):
    job_schema = JobSchema()

    data = job_schema.dump(job_db_obj)

    return data
