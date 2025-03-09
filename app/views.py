from django.shortcuts import render,HttpResponse
from django.shortcuts import render
import pathlib
from . models import PageVisit
# Create your views here.
this_dir=pathlib.Path(__file__).resolve().parent
def home(request,*args,**kwargs):
    qs=PageVisit.objects.all()
    page_qs= PageVisit.objects.filter(path=request.path)

    my_title = "Hello there..."
    my_context = {
        "title": my_title,
        "query_set_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percentage": (page_qs.count()/qs.count())*100
    }

    path = request.path
    print('path',path)
    html_template = "index.html"
    PageVisit.objects.create(path=request.path)
    return render(request,html_template,my_context)