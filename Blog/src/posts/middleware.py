from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
class SimpleMiddleWare(MiddlewareMixin):
	def process_request(self, request):
		print("SimpleMiddleWare executed")

	def process_response(self, request, response):
		print("SimpleMiddleWare response")
		return response

class AnotherMiddleware(MiddlewareMixin):
	def process_request(self, request):
		print ("AnotherMiddleware executed")

	def process_response(self, request, response):
		print ("AnotherMiddleware response")
		return response