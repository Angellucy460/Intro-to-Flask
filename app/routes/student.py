from flask import Blueprint, jsonify, request


#create student blueprint
student_bp = Blueprint("student", __name__, url_prefix="/student")


    

#routes and controller logic
@student_bp.route("/add", methods=["POST"])
def add_user():
    print("add user was hit")
    return "adding a user"

@student_bp.route("/edit", methods=["PUT"])
def edit_student():
    print("add user was hit")
    return "Edit a student"

@student_bp.route("/list", methods=["GET"])
def list_users():
    print("List Students")
    return "List all students"
