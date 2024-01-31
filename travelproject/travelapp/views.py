from django.http import HttpResponse
from django.shortcuts import render

from .models import Place, Team


# def demo(request):
#   name = "india"
#  return render(request, "index.html", {'obj': name})

def demo1(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})



# def demo2(request):
#
#     return render(request, "index.html", {'result1': obj1})
# def addition(request):
#   x = int(request.GET['number1'])
#  y = int(request.GET['number2'])
# res = x + y
# return render(request, 'add.html', {'result': res})


# def about(request):
#   name = "kerala"
#  return render(request, "about.html", {'obj': name})
# def menu(request):
#   return render(request,'menu.html')
# def thanks(request):
#   return HttpResponse("thank you")
