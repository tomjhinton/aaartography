from app import db
from pony.orm import Required, Optional, Set
from marshmallow import Schema, fields, post_load
from datetime import datetime, timedelta




class Submission(db.Entity):
    artist = Required(str)
    title = Required(str)
    cover = Optional(str)
    description = Required(str)



class SubmissionSchema(Schema):
    id = fields.Int(dump_only=True)
    artist = fields.Str(required=True)
    title = fields.Str()
    cover = fields.Str()
    description = fields.Str(required=True)
