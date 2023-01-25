from server.instance import server
from controllers.user_code_controller import UserController
from controllers.user_controller import UsersListController
from ma import ma
from db import db


api = server.api
app = server.app

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(UserController, '/Users/<int:id>')
api.add_resource(UsersListController, '/Users')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()