from django.shortcuts import render
from django.http import HttpResponse

from .tasks import email_welcome

def home(request):
    if request.POST:
        email_welcome.delay(to="pytuxi@gmail.com")
        return HttpResponse('sended email')
    else:
        return render(request, "myapp/index.html")
