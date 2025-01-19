from http import HTTPStatus

from src.app import db, Role
from flask import Blueprint, request

app = Blueprint('role', __name__, url_prefix="/roles")


@app.route('/', methods=["POST"])
def create_role():
    data = request.json
    role = Role(name=data["name"])
    db.session.add(role)
    db.session.commit()
    return {"message": "Role created!"}, HTTPStatus.CREATED
