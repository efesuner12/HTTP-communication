from flask import request
from flask_restful import Resource

import subprocess

from app.authentication import Authentication

class Commands(Resource):
    
    def get(self, command):
        token = request.json.get('token')

        authObj = Authentication()
        is_valid_token = authObj.valid_auth_token(token)

        if is_valid_token == True:
            if command.lower() == "hello":
                return 'Hello, friend.', 200
            elif command.lower() == "sysinfo":
                try:
                    sys_info = subprocess.getoutput(['systeminfo'])
                    return {"System Info:": sys_info}, 200
                except Exception as e:
                    return f"There has been an error executing the command! Error message: {e}", 500
            else:
                return 'Not a valid command', 404
        else:
            return str(is_valid_token[0]), is_valid_token[1]
