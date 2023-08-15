from app.commands import Commands
from app.authentication import Authentication

def initialise_routes(api):
    api.add_resource(Commands, '/api/v1/commands/<command>')
    api.add_resource(Authentication, '/api/v1/auth')
