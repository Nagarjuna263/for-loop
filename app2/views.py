from django.shortcuts import render

# Create your views here.
def forloop(request):
    d=context={'age':'nag','price':20}
    return render(request,'forloop.html',d)