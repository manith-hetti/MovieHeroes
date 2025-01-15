import jwt
import datetime
import os

SECRET_KEY = os.getenv('JWT_SECRET')

def generate_token(user_id):
    """
    Generate a JWT token for a specific user.
    """
    payload = {
        'user_id': user_id,
        'iat': datetime.datetime.now(datetime.UTC),
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=10)  # Token expires in 10 minutes
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    print("We got this far in generating a token")
    return token

def decode_token(token):
    """
    Decode a JWT token.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token
