from django.urls import path

from . import views

# from . import views
#можно так:
#from .views import home_page_view



urlpatterns = [
    path("", views.home_page_view),
]