from django.shortcuts import render, HttpResponse
import pathlib
from .models import PageVisit

# Get the current directory
this_dir = pathlib.Path(__file__).resolve().parent

def home(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    my_title = "Hello there..."
    total_count = qs.count()
    page_count = page_qs.count()

    percentage = (page_count / total_count) * 100 if total_count > 0 else 0  # Avoid ZeroDivisionError

    my_context = {
        "title": my_title,
        "query_set_count": page_count,
        "total_visit_count": total_count,
        "percentage": percentage
    }

    print('Path:', request.path)
    PageVisit.objects.create(path=request.path)
    return render(request, "index.html", my_context)

def about(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    total_count = qs.count()
    page_count = page_qs.count()
    try:
        percentage = (page_count / total_count) * 100 if total_count > 0 else 0  # Avoid ZeroDivisionError
    except:
        percentage = 0
    my_title = "About Page"
    my_context = {
        "title": my_title,
        "query_set_count": page_count,
        "total_visit_count": total_count,
        "percentage": percentage
    }

    print('Path:', request.path)
    PageVisit.objects.create(path=request.path)
    return render(request, "about.html", my_context)
