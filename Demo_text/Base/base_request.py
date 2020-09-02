# coding = utf-8
import requests


class BaseRequest(object):
	# def __init__(self, url, data):
	# 	self.url = url
	# 	self.data = data

	@staticmethod
	def send_post(url, post_data):
		# post请求
		try:
			res = requests.post(url=url, data=post_data)
			return res
		except Exception as e:
			return e

	@staticmethod
	def send_get(url, get_data):
		# get请求
		try:
			res = requests.get(url=url, params=get_data)
			return res
		except Exception as e:
			return e

	def run_main(self, method, url, run_data):
		"""
		传递method url run_data 参数
		:param method:
		:param url:
		:param run_data:
		:return:返回请求的数据
		"""
		if method == 'get':
			res = self.send_get(url, run_data)
			return res
		elif method == 'post':
			res = self.send_post(url, run_data)
			return res
			pass
		else:
			return "方法错误"


post_login_url = "http://127.0.0.1:5000/get/user/login"
data = {
    "username": 1,
    "password": 2,
    "token": 123
}
a = BaseRequest()
print(a.run_main("get", url=post_login_url, run_data=data).status_code)
