from django.urls import path
from shop.views import *
app_name='shop'
urlpatterns = [

    path('', IndexView.as_view(template_name="shop/index.html"),name='index'),
    # path ('about/',about_view,name='about'),
    path ('contact/',ContactFormView.as_view(),name='contact'),
    #path('test',test,name='test')
    path('product/<int:pk>',ProductDetailView.as_view(template_name="shop/product_view.html"),name= "ProductView"),
    
]