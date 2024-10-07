from django.shortcuts import render
from myapp.models import tech
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def index(request):
  if request.method == "POST":
    data = request.POST
    new = tech(name = data["field1"], cost = data["field2"], count = data["field3"], description = data["field4"], category = data["field5"])
    new.save()
  res = tech.objects.all()
  print(res)
  return render(request,"index.html", {"test":res})




def reg(request):
  if request.method == "POST":
    data = request.POST
    user = User.objects.create_user(data["login"],data["email"], data["psw"])
    user.save()
    print(data)
  return render(request,"reg.html")




def auth(request):
  if request.method == "POST":
    data = request.POST
    user = authenticate(request, username = data["login"], password = data["psw"])
    if user :
      login(request,user)
    else:
      return HttpResponse("wrong login or password")

  print(request.user.is_authenticated)
  return render(request,"reg.html")






def main(request):
  data = tech.objects.all()
  return render(request, "main.html", {"res":data})