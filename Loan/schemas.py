from marshmallow import Schema, fields


class LoanSchema(Schema):
    id = fields.Int(dump_only=True)
    loan_type = fields.Str(required=True)
    loan_amount = fields.Float(required=True)
    date = fields.Date(required=True)
    rate_of_interest = fields.Int(required=True)
    duration = fields.Float(required=True)
    customer_id = fields.Int(dump_only=True)

# class LoanSchemawithUser(LoanSchema):
#     # customer = fields.List(fields.Nested(LoanSchema()), dump_only=True)    

