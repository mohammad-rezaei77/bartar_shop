from django.shortcuts import render
from django.views.generic import TemplateView, FormView,DetailView
from django.views.generic.list import ListView 
from .models import Product ,Brand ,Category
from shop.forms import ContactForm
# Create your views here.






class IndexView(TemplateView):
    ordering = ['id',]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["categorys"] = Category.objects.all()
        context ["brands"] = Brand.objects.all()[:10]        
        context ['products_featured'] = Product.objects.filter(status=True,
                                                               tags__name = "featured").order_by('created_at')[:5]
        context ['products_top_sale'] = Product.objects.filter(status=True).order_by('-salesـnumber')[:5]
        context ['products_top'] = Product.objects.filter(status=True).order_by('-rate')[:5]
        context ['specialـdiscount'] = Product.objects.filter(status=True,
                                                              tags__name = "discount").order_by('created_at')[:2]
        context ["vije_products"] = Product.objects.filter(status=True,tags__name = "vije")[:5]
        context ["poremriaz_products"] = Product.objects.filter(status=True).order_by('salesـnumber')[:6]
        
        return context
  
  
  
        
class ProductDetailView(DetailView) :
    model = Product
    context_object_name = "Product"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_param= str(self.request)
        context ["similars"] = Product.objects.filter(category_id = category_param[31])[:4]
        context ["categorys"] = Category.objects.all()
        
        return context
  
  
  
    
class CategoryDetailView(TemplateView): 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["categorys"] = Category.objects.all()
        context ['cat_products'] = Product.objects.filter(status=True)
        
        return context
      
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
class ContactFormView(FormView):
    template_name = 'shop/contact.html'
    form_class = ContactForm
    success_url = '/index/'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)