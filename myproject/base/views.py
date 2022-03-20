from django.http import request,HttpResponse
from django.shortcuts import render
from django.template import loader
def index(request):
    return HttpResponse('<h2> Hello world </h2>')

def contact(request):
    return render(request, 'C:\\Users\\compu\\Desktop\\Python\\django\\myproject\\base\\templates\\test.html')
