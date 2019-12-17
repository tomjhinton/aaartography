from flask import Blueprint, request, jsonify, abort, g
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Submission import Submission, SubmissionSchema
from lib.secure_route import secure_route


router = Blueprint(__name__, 'submissions')

@router.route('/submissions', methods=['GET'])
@db_session
def index():
    schema = SubmissionSchema(many=True)
    submissions = Submission.select()
    return schema.dumps(submissions)


@router.route('/submissions', methods=['POST'])
@db_session
@secure_route
def create():
    schema = SubmissionSchema()

    try:
        data = schema.load(request.get_json())
        submission = Submission(**data, createdBy=g.current_user)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(submission), 201


@router.route('/submissions/<int:submission_id>', methods=['GET'])
@db_session
def show(submission_id):
    schema = SubmissionSchema()
    submission = Submission.get(id=submission_id)

    if not submission:
        abort(404)

    return schema.dumps(submission)


@router.route('/submissions/<int:submission_id>', methods=['PUT'])
@db_session
@secure_route
def update(submission_id):
    schema = SubmissionSchema()
    submission = Submission.get(id=submission_id)

    if not submission:
        abort(404)

    try:
        data = schema.load(request.get_json())
        submission.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(submission)


@router.route('/submissions/<int:submission_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(submission_id):
    submission = Submission.get(id=submission_id)

    if not submission:
        abort(404)

    submission.delete()
    db.commit()

    return '', 204
