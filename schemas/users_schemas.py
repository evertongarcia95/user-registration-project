from ma import ma
from models.users_model import UserModel
from marshmallow import fields

class UsersSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = UserModel
            load_instance = True