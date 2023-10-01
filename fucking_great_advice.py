import requests
class Client():
	def __init__(self):
		self.api="https://fucking-great-advice.ru/api/v2"
		self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
	def random_advices(self):
		return requests.get(f"{self.api}/random-advices",headers=self.headers).json()
	def random_advices_by_tag(self,tag):
		return requests.get(f"{self.api}/random-advices-by-tag?tag={tag}",headers=self.headers).json()