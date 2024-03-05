from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request: WSGIRequest):
    if request.method == "GET":
        return render(request, "speaker/index.html")
    elif request.method == "POST":
        print(request.POST["input_text"])
        # return HttpResponse("got here")
        return render(request, "speaker/output.html")
    else:
        response = HttpResponse(
            f"{request.method} not allowed on {request.path}")
        response.status_code = 405
        return response


def contact(request: WSGIRequest):
    if request.method == "POST":
        return HttpResponse("recieved contact ping")
    else:
        response = HttpResponse(
            f"{request.method} not allowed on {request.path}")
        response.status_code = 405
        return response
