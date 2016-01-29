from django.http import HttpResponse
def homeTemplate(request):
	return HttpResponse("Hello World!")