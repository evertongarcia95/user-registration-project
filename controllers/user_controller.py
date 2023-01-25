
from flask import request
from flask_restplus import Resource, fields
from exceptions.custom_errors import CustomError
from swagger import responses_constants, users_response
from schemas.users_schemas import UsersSchema
from server.instance import server
from services.user_service import UserService

user_ns = server.user_ns

user_schema = UsersSchema()

item = user_ns.model('User',{
    'username': fields.String(decription= 'Name user indentification'),
    'password': fields.String(decription= 'Passord the user'),
    'name': fields.String(decription= 'name and surname'),
    'email': fields.String(decription= 'Email')
})

@user_ns.route(methods=['POST', 'GET'])
class UsersListController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService()

    @user_ns.response(200, 'RESPONSE_STATUS_CODE_200', users_response.get_users_response_200)
    @user_ns.response(500, 'RESPONSE_STATUS_CODE_500', users_response.get_users_response_error_500)
    def get(self,):
        try:
            users = self.user_service.get_users()
            return user_schema.dump(users, many=True)
        
        except CustomError as ex:
            return {"message": ex.message}, ex.status
        
        except Exception as ex:
            logger_exception(request, str(ex), 'Get users', request.json)
            return {"message": responses_constants.GET_USERS_ERROR_500}, 500 

    @user_ns.response(200, 'RESPONSE_STATUS_CODE_200', users_response.post_user_response_200)
    @user_ns.response(404, 'RESPONSE_STATUS_CODE_404', users_response.post_user_response_error_400)
    @user_ns.response(500, 'RESPONSE_STATUS_CODE_500', users_response.post_user_response_error_500)
    @user_ns.expect(item)
    @user_ns.doc('Create an user')
    def post(self):
        try:
            request_body = dict(request.json)
            return self.user_service.create_user(request_body)
        
        except CustomError as ex:
            return {"message": ex.message}, ex.status
        
        except Exception as ex:
            logger_exception(request, str(ex), 'Create user', request.json)
            return {"message": responses_constants.POST_USER_ERROR_500}, 500 
