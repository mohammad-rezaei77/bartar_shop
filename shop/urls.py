from django.urls import path
from shop.views import *
app_name='shop'
urlpatterns = [

    path('', IndexView.as_view(template_name = "shop/index.html"),name='index'),
    # path ('about/',about_view,name='about'),
    path ('contact/',ContactFormView.as_view(),name = 'contact'),
    path ('product/<str:slug>',ProductDetailView.as_view(template_name="shop/product_view.html"),name = "ProductView"),
    path ('category/<str:slug>',CategoryDetailView.as_view(template_name="shop/category_detail.html"),name = "CategoryDetail" ),
    
]