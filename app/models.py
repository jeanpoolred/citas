from . import db

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    doctor_name = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(200))

    def to_dict(self):
        return {
            'id': self.id,
            'patient_name': self.patient_name,
            'doctor_name': self.doctor_name,
            'appointment_time': self.appointment_time.isoformat(),
            'description': self.description
        }
from flask_sqlalchemy import SQLAlchemy  db = SQLAlchemy() 
