from app import app
from flask import request, jsonify
from lib.user_repository import *
from lib.user import User
from lib.database_connection import get_db

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    print(data)

    if not email or not password:
        return jsonify({'error': 'Please provide email, and password'}), 400

    db = get_db()
    user_repo = UserRepository(db)

    user_check = user_repo.user_exists(email,password)

    return user_check

