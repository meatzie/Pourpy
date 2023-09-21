from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Welcome! Have a dashboard!")


def dashboarder(request, name):
    print(request.build_absolute_uri())
    return render(
        request, "dashboard/dashboard.html", {"name": name, "date": datetime.now()}
    )
