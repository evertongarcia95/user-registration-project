from flask import request
from flask_restplus import Resource, fields
from exceptions.custom_errors import CustomError
from swagger import responses_constants, users_response
from schemas.users_schemas import UsersSchema
from server.instance import server
from services.user_service import UserService

user_ns = server.user_ns

user_schema = UsersSchema()
users_list_schemas = UsersSchema(many=True)

item = user_ns.model('User',{
    'username': fields.String(decription= 'Name user indentification'),
    'password': fields.String(decription= 'Passord the user'),
    'name': fields.String(decription= 'name and surname'),
    'email': fields.String(decription= 'Email')
})

@user_ns.route(methods=['GET', 'PUT', 'DELETE'])
class UserController(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService()

    @user_ns.response(200, 'RESPONSE_STATUS_CODE_200', users_response.get_user_response_200)
    @user_ns.response(404, 'RESPONSE_STATUS_CODE_404', users_response.user_not_found_error_404)
    @user_ns.response(500, 'RESPONSE_STATUS_CODE_500', users_response.get_user_response_error_500)
    def get(self, id):
        try:
            return self.user_service.get_user(id)
        
        except CustomError as ex:
            return {"message": ex.message}, ex.status
        
        except Exception as ex:
            logger_exception(request, str(ex), 'Get user', request.json)
            return {"message": responses_constants.GET_USER_ERROR_500}, 500 

    @user_ns.response(200, 'RESPONSE_STATUS_CODE_200', users_response.put_user_response_200)
    @user_ns.response(404, 'RESPONSE_STATUS_CODE_404', users_response.user_not_found_error_404)
    @user_ns.response(500, 'RESPONSE_STATUS_CODE_500', users_response.put_user_response_error_500)
    @user_ns.expect(item)
    def put(self, id):
        try:
            request_body = dict(request.json)
            return self.user_service.update_user(id, request_body)
        
        except CustomError as ex:
            return {"message": ex.message}, ex.status
        
        except Exception as ex:
            logger_exception(request, str(ex), 'Update user', request.json)
            return {"message": responses_constants.PUT_USER_ERROR_500}, 500 



    @user_ns.response(200, 'RESPONSE_STATUS_CODE_200', users_response.delete_user_response_200)
    @user_ns.response(404, 'RESPONSE_STATUS_CODE_404', users_response.user_not_found_error_404)
    @user_ns.response(500, 'RESPONSE_STATUS_CODE_500', users_response.delete_user_response_error_500)
    def delete(self, id):
        try:
            return self.user_service.delete_user(id)
        
        except CustomError as ex:
            return {"message": ex.message}, ex.status
        
        except Exception as ex:
            logger_exception(request, str(ex), 'Delete user', request.json)
            return {"message": responses_constants.DELETE_USER_ERROR_500}, 500 



