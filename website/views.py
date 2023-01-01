from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index_view(request):                              
    return render(request,"website/index.html")

class IndexView(TemplateView):
    template_name = "website/index.html"