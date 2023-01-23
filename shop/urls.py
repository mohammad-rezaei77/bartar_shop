from django.urls import path
from shop.views import *
app_name='website'
urlpatterns = [

    path('', IndexView.as_view(template_name="shop/index.html")),
    # path ('about/',about_view,name='about'),
    # path ('contact/',contact_view,name='contact'),
    #path('test',test,name='test')
    
]