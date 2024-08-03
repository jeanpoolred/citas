from flasgger import Swagger
from app import create_app, db
from app.routes import appointments_blueprint

app = create_app()
swagger = Swagger(app)

with app.app_context():
    db.create_all()

app.register_blueprint(appointments_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
