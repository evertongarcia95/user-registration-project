from flask_restplus import fields
from server.instance import server
from swagger import responses_constants

api = server.api


get_user_response_200 = ('GetUserResponse200', {
"message": fields.String(example='')
})

user_not_found_error_404 = ('UserNotFoundError404', {
"message": fields.String(example=responses_constants.USER_NOT_FOUND_404)
})

get_user_response_error_500 = ('GetUserResponseError500', {
"message": fields.String(example=responses_constants.GET_USER_ERROR_500)
})

put_user_response_200 = ('PutUserResponse200', {
"message": fields.String(example=responses_constants.PUT_USER_UPDATE)
})

put_user_response_error_500 = ('PutUserResponseError500', {
"message": fields.String(example=responses_constants.PUT_USER_ERROR_500)
})

delete_user_response_200 = ('DeleteUserResponse200', {
"message": fields.String(example=responses_constants.USER_DELETE)
})

delete_user_response_error_500 = ('DeleteUserResponseError500', {
"message": fields.String(example=responses_constants.DELETE_USER_ERROR_500)
})

get_users_response_200 = ('GetUsersResponse200', {
"message": fields.String(example='')
})

get_users_response_error_500 = ('GetUsersResponseError500', {
"message": fields.String(example=responses_constants.GET_USERS_ERROR_500)
})

post_users_response_200 = ('PostUserResponse200', {
"message": fields.String(example=responses_constants.POST_USER_REGISTERED)
})

post_user_response_error_500 = ('PostUsersResponseError500', {
"message": fields.String(example=responses_constants.POST_USER_ERROR_500)
})
