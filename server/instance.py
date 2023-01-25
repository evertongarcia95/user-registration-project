from flask import Flask, Blueprint
from flask_restplus import Api


class Server():
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint,
            doc='/docs',
            info='System for registering and handling user data.',
            title='User registration data Project Documentation.',
            version='1.0',
            description='System for registering and handling user data.'
        )
        self.app.register_blueprint(self.blueprint)
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.user_ns = self.user_ns()

    def user_ns(self, ):
        return self.api.namespace(
            name='Users',
            description='Responsible for creating, reading, updating, deleting user data.',
            path='/'
        )

    def run(self,):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )

server = Server()