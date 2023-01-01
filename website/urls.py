from django.urls import path
from website.views import *
app_name='website'
urlpatterns = [

    path('', IndexView.as_view(template_name="website/index.html")),
    # path ('about/',about_view,name='about'),
    # path ('contact/',contact_view,name='contact'),
    #path('test',test,name='test')
    
]