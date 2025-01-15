from app import app
from flask import request, jsonify
from lib.user_repository import *
from lib.user import User
from lib.database_connection import get_db

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')

    if not full_name or not email or not password :
        return jsonify({'error': 'Please provide full name, email, and password'}), 400

    db = get_db()
    user_repo = UserRepository(db)

    email_check = user_repo.email_exists(email)

    if email_check == True:
        email_error = user_repo.user_details_errors['email']
        return jsonify({'email_exist': email_error}),500
    else:
        user = User(full_name, email, password)
        new_user = user_repo.create(user)
        return jsonify({
                'id': str(new_user.id),
                'full_name': new_user.full_name,
                'email': new_user.email,
            }), 201
