import requests
home_url = "http://127.0.0.1:5000/"
test = requests.get(url=home_url)
print(test.text)


get_login_url = "http://127.0.0.1:5000/get/user/login?username=1&password=2"
test = requests.get(url=get_login_url)
print(test.text)

post_login_url = "http://127.0.0.1:5000/post/user/login"
data = {
    "username": 1,
    "password": 2,
    "token": 123
}
test = requests.post(url=post_login_url, data=data)
print(test.text)
