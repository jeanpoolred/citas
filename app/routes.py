from flask import Blueprint, jsonify, request
from datetime import datetime
from flasgger import swag_from
from . import db
from .models import Appointment

appointments_blueprint = Blueprint('appointments', __name__)

@appointments_blueprint.route('/appointments', methods=['GET'])
@swag_from('../swagger/add_appointment.yml', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([appointment.to_dict() for appointment in appointments])

@appointments_blueprint.route('/appointments', methods=['POST'])
@swag_from('../swagger/add_appointment.yml', methods=['POST'])
def create_appointment():
    data = request.get_json()
    appointment_time = datetime.fromisoformat(data['appointment_time'])
    new_appointment = Appointment(
        patient_name=data['patient_name'],
        doctor_name=data['doctor_name'],
        appointment_time=appointment_time,
        description=data.get('description')
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify(new_appointment.to_dict()), 201

@appointments_blueprint.route('/appointments/<int:id>', methods=['GET'])
def get_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    return jsonify(appointment.to_dict())

@appointments_blueprint.route('/appointments/<int:id>', methods=['PUT'])
def update_appointment(id):
    data = request.get_json()
    appointment = Appointment.query.get_or_404(id)
    appointment.patient_name = data['patient_name']
    appointment.doctor_name = data['doctor_name']
    appointment.appointment_time = datetime.fromisoformat(data['appointment_time'])
    appointment.description = data.get('description')
    db.session.commit()
    return jsonify(appointment.to_dict())

@appointments_blueprint.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    db.session.delete(appointment)
    db.session.commit()
    return '', 204
