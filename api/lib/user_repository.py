from lib.user import User
import bcrypt
from lib.database_connection import get_db
from flask import jsonify
from lib.token import *
from bson import ObjectId

class UserRepository():
    def __init__(self, db):
        self.db = db
        self.user_details_errors = {'password': "", 'email': "" , "login" : ""}

    #Create a new user
    #user: an instance of User class object
    def create(self, user, table_name = 'users'):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), salt)

        highest_user_id = self.get_highest_user_id()
        next_user_id = 611 if highest_user_id is None else highest_user_id + 1

        user_data = {
            'full_name': user.full_name,
            'email': user.email,
            'password': hashed_password.decode("utf-8") ,
            'userId': next_user_id,
            'avatar' : "src/assets/default_pic.png"
        }
        result = self.db[table_name].insert_one(user_data)
        print("Table created")
        user.id = result.inserted_id
        user.password = hashed_password.decode("utf-8")
        # Why are we returning this user? - Manith
        return user

    #Checks if the user already exists in our db
    def email_exists(self, email, table_name = 'users'):
        user = self.db[table_name].find_one({'email': email})
        if user:
            self.user_details_errors['email'] = "Email address already exists. Try another one!"
            return True
        return False

#Check if the password already exists in our DB
    def user_exists(self,email, password):
        print("We're checking if user exists")
        user = self.db.users.find_one({'email': email})

        if not user:
            print("Auth Error: User not found")
            return jsonify({"message": "User not found"}), 401
        elif not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            print("Auth Error: Passwords do not match")
            return jsonify({"message": "Password incorrect"}), 401
        else :
            user_id_str = str(user['_id'])
            token = generate_token(user_id_str)
            print("we have the token")
            return jsonify({"token": token, "message": "OK", "userId": str(user['_id']),"full_name": user['full_name'], "email": user['email'], "user_id": user["userId"]}), 201
            # James: Added in full_name and email to JSON to be able to use for "Myprofile" page

    def get_highest_user_id(self):
        highest_user = self.db.users.find_one(sort=[("userId", -1)])
        if highest_user:
            return highest_user['userId']
        return None

    def find_user_by_id(self,id, users = "users"):
        users = self.db[users]
        found_user = users.find_one({"_id":ObjectId(id)})
        return found_user

    def update_avatar_by_id(self,id,avatar, users = "users"):
        users = self.db["users"]
        result = users.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'avatar': avatar}}
        )
        return result

    def get_user_id_from_object_id(self, objectId):
        users = self.db["users"]
        user = self.db.users.find_one({"_id": ObjectId(objectId)})
        return user['userId']
