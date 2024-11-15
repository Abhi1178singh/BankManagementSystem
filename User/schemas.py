from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    address = fields.Str(required=True)
    state = fields.Str(required=True)
    country = fields.Str(required=True)
    email = fields.Email(required=True)
    pan = fields.Str(required=True)
    contact_no = fields.Int(required=True)
    dob = fields.Date(required=True)
    account_type = fields.Str(required=True)

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    

