from models.users_model import UserModel
from exceptions.custom_errors import NotFound
from swagger import responses_constants


class UserService():
    def __init__(self) -> None:
        self.user_model = UserModel()

    def get_user(self, id):
        user_data = self.user_model.find_by_id(id)
        if user_data:
            return user_data, 201
        raise NotFound(message=responses_constants.USER_NOT_FOUND_404)
    
    def update_user(self, id, request_body):
        user_data = self.user_model.find_by_id(id)

        if not user_data:
            raise NotFound(message=responses_constants.USER_NOT_FOUND_404)

        user_data.username = request_body['username']
        user_data.password = request_body['password']
        user_data.name = request_body['name']
        user_data.email = request_body['email']

        user_data.save_to_db()

        return {'message': responses_constants.PUT_USER_UPDATE}
    
    def delete_user(self, id):
        user_data =self.user_model.find_by_id(id)
        if user_data:
            user_data.delete_from_db()
            return {'message': responses_constants.USER_DELETE}
        
        raise NotFound(message=responses_constants.USER_NOT_FOUND_404)
    
    def get_users(self):
        return self.user_model.find_all()
    
    def create_user(self, request_body):
        user_data = request_body.load(request_body)
        user_data.save_to_db()

        return {'message': responses_constants.POST_USER_REGISTERED}


