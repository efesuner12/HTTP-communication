# HTTP-communication
A command-server implemented through an API.

Example usage:
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"admin"}' http://127.0.0.1:8080/api/v1/auth

curl -i -X GET -H "Content-Type: application/json" -d '{"token":"<TOKEN>"}' http://127.0.0.1:8080/api/v1/commands/hello
