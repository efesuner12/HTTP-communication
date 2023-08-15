# HTTP-communication
A command-server implemented through an API.

Setup:\n
git clone git@github.com:efesuner12/HTTP-communication.git
cd HTTP-communication
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

Example usage:
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"admin"}' http://127.0.0.1:8080/api/v1/auth

curl -i -X GET -H "Content-Type: application/json" -d '{"token":"<TOKEN>"}' http://127.0.0.1:8080/api/v1/commands/hello
