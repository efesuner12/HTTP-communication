from flask import request
from flask_restful import Resource
from datetime import datetime, timedelta

import jwt

import app.cryptography as crypto

class Authentication(Resource):

    def __init__(self) -> None:
        self.USERNAME = "admin"
        self.PASSWORD = "4bf4d11ec0985b52accd598a34420b44f0dfa02f7637595ddf064b487163910998167d63f1581c7a4ab51e945851a194eab75cc1a7c3d27e11ea57f4556f3f570876d71e24f13335ed2282522e271cd7"
        self.EXPIRE_DELTA = 60
        self.SECRET_KEY = "326191a4070ce0672e473e31f0389a3a517b13f83597aabe1daa2841c3b9c90e"

    def generate_auth_token(self):
        current = datetime.now()
        time_change = timedelta(minutes=self.EXPIRE_DELTA)

        expire_time = current + time_change
        expire_time = expire_time.timestamp()

        return jwt.encode({'id':"admin", 'exp':expire_time}, self.SECRET_KEY, algorithm='HS256')

    def valid_auth_token(self, token):
        if not token:
            return ["No token has been provided", 401]

        try:
            decoded = jwt.decode(token, self.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError as e:
            return ["Your token has expired! Please re login", 401]
        except Exception as e:
            return [f"There has been an error with the token! Error message: {e}", 500]
        
        return decoded['id'] == "admin"

    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        
        if username and password:
            if username == self.USERNAME and crypto.validate_hash(password, self.PASSWORD):
                token = self.generate_auth_token()

                return f"Welcome! Your access token is: '{token}'", 200
            else:
                return "Incorrect username or password", 401
        else:
            return "No username or password has been provided", 400
