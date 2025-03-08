from django.shortcuts import render
from django.shortcuts import render
import pathlib
# Create your views here.
def home(request,*args,**kwargs):
    my_title = "Hello there..."
    my_context = {
        "title":my_title
    }
    html_template = "index.html"
    return render(request, 'index.html', my_context)