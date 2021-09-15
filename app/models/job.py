from datetime import datetime

from app import db

Column = db.Column
Model = db.Model


class Job(Model):
    """ Job model for storing job related data """

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(64))
    created = Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super(Job, self).__init__(**kwargs)

    def __repr__(self):
        return f"<Job {self.id}: {self.name}>"
