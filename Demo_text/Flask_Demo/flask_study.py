# coding=utf-8
from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/')
def home():
    data = json.dumps({
        'username': 'home username',
        'password': 'home password'
    })
    return data


@app.route('/get/user/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        data = json.dumps({
            'username': username,
            'password': password
        })
    else:
        data = json.dumps({
            "messgae": "请传参数"
        })
    return data


@app.route('/post/user/login', methods=['POST'])
def post_login():
    request_method = request.method
    if request_method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        token = request.form.get("token")
        data = json.dumps({
            'username': username,
            'password': password,
            'token': token
        })
        pass
    else:
        data = json.dumps(
            {
                'message': '请求不和法'
            }
        )
    return data


if __name__ == "__main__":
    app.run()
