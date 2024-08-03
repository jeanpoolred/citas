import unittest
import json
from app import create_app, db
from app.models import Appointment

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_appointment(self):
        response = self.client.post('/appointments', json={
            "patient_name": "John Doe",
            "doctor_name": "Dr. Smith",
            "appointment_time": "2024-08-01T10:00:00",
            "description": "Routine checkup"
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['patient_name'], "John Doe")

    def test_get_appointments(self):
        response = self.client.get('/appointments')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
