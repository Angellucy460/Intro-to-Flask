from flask import Blueprint, jsonify, request


#create student blueprint
student_bp=Blueprint("student",__name__)


    

#routes and controller logic
@student_bp.route("/student/add", methods=["POST"])
def add_user():
    print("add user was hit")
    return "adding a user"

@student_bp.route("/student/list", methods=["GET"])
def list_user():
    print("Lists Students")
    return "List all students"
