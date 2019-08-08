from django.http import HttpResponse
from django.shortcuts import render


def home_view(request,*args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>Hello Ing. Duvan Mejia </h1>") #string of HTML code
    return render(request, "home.html", {})

def about_view(request,*args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 8080,
        "this_is_true":True,
        "my_list":[123, 8080, 12345, 8000, "Duvan"]
    }
    return render(request, "about.html", my_context)
