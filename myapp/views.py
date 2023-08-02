from django.shortcuts import render
# Create your views here.
 


def index(request):
    return render(request,'index.html')


def counter(request):
    if request.method == 'POST':
        txt=request.POST['txt']
        l=len(txt.split())    
    return render(request,'counter.html',{'l':l})