from django.urls import path
from . import views

# django's default logout 
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [

    path("", views.home, name="index"),
    path("shop_all", views.shop, name="shop"),
    path("blogs", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),

    # authentication 
    path("login/", views.CustomLoginView.as_view(), name='login'),
    path("sign-up/", views.register, name='sign-up'),
    # path("logout/", LogoutView.as_view(next_page='login'), name='logout'),
    path("logout/", views.logout_view, name="logout"),

    # path("password-reset/", PasswordResetView.as_view(template_name='registration/password_reset.html', email_template_name='registration/password_reset_email.html'), name='password_reset',),
    # """Modified password reset functionality""",
    path("password-reset/", views.CustomPasswordResetView.as_view(), name='password_reset'),
    path("password-reset/done/", PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
]
