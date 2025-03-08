from django.shortcuts import render

# Create your views here.
def home(request,*args,**kwargs):
    my_title = "Hello there..."
    return render(request, 'index.html', {"title":my_title})