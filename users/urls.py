from django.urls import path
from . import views

# django's default logout 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="index"),
    path("shop_all", views.shop, name="shop"),
    path("blogs", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    # authentication 
    path("login/", views.CustomLoginView.as_view(), name='login'),
    path("sign-up/", views.register, name='sign-up'),
    path("logout/", LogoutView.as_view(next_page='login'), name='logout'),
]
