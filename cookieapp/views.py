from django.http import  HttpResponse
from django.shortcuts import render
def input(request):
    return  render(request,'base.html')
def add(request):
    x=int(request.GET['t1'])
    y=int(request.GET['t2'])
    z=x+y
    resp=HttpResponse('values submited successfully')
    resp.set_cookie('z',z,max_age=50)
    return resp
def display(request):
    for a,b in request.COOKIES.items():
        print(a,b)
    if 'z' in request.COOKIES:
        sum = request.COOKIES['z']
        return HttpResponse("adition of two no:" +sum)
    else:
        return render(request,'base.html')


