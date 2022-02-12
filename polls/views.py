from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You're at the polls index.こんにちは世界!!")

# Create your views here.
