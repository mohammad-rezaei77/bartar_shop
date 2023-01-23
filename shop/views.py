from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Product
# Create your views here.

# def index_view(request):                              
#     return render(request,"website/index.html")

class IndexView(ListView):
    # template_name = "shop/index.html"
    model = Product
    paginate_by = 12
    context_object_name = "Products"
    ordering = ['id',]
    
    
    
    
    
# Create your views here.

# def index_view(request):                              
#     return render(request,"website/index.html")

# class IndexView(TemplateView):
#     template_name = "shop/index.html"