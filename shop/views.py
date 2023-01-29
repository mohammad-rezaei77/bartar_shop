from django.shortcuts import render
from django.views.generic import TemplateView, FormView,DetailView
from django.views.generic.list import ListView 
from .models import Product ,Brand
from shop.forms import ContactForm
# Create your views here.

# def index_view(request):                              
#     return render(request,"website/index.html")

class IndexView(TemplateView):
    # queryset = Product.objects.filter(status=True)
    # context_object_name = "products"
    ordering = ['id',]
    # paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["products"] = Product.objects.filter(status=True)
        context ["best_products"] = Product.objects.filter(status=True)[:3]
        context ["vije_products"] = Product.objects.filter(status=True,tags__name = "vije")
        context ["poremriaz_products"] = Product.objects.filter(status=True,tags__name = "poremroz")
        context ["brands"] = Brand.objects.all()
        
        
        return context
        
class ProductDetailView(DetailView) :
    model = Product
    context_object_name = "Product"
    

 
    
class ContactFormView(FormView):
    template_name = 'shop/contact.html'
    form_class = ContactForm
    success_url = '/index/'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
    
    

    
    
    
    
# Create your views here.

# def index_view(request):                              
#     return render(request,"website/index.html")

# class IndexView(TemplateView):
#     template_name = "shop/index.html"