
from django.http import HttpResponse
def home(request):
    return HttpResponse("This is a page.My name is django")

def contact(request):
    return HttpResponse("This is contact page")