# HTTP-communication
A command-server implemented through an API.

<b>Setup:</b><br />
git clone git@github.com:efesuner12/HTTP-communication.git<br />
cd HTTP-communication<br />
python3 -m venv venv<br />
source venv/bin/activate<br />
pip3 install -r requirements.txt<br />

<b>Example usage:</b><br />
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"admin"}' http://127.0.0.1:8080/api/v1/auth

curl -i -X GET -H "Content-Type: application/json" -d '{"token":"<TOKEN>"}' http://127.0.0.1:8080/api/v1/commands/hello
