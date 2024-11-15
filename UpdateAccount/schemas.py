from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str(load_only=True)
    address = fields.Str()
    state = fields.Str()
    country = fields.Str()
    email = fields.Email()
    pan = fields.Str()
    contact_no = fields.Int()
    dob = fields.Date()
    account_type = fields.Str()


