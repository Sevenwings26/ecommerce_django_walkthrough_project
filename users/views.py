from django.shortcuts import render
from .models import User
from products.models import Product, Category
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordResetView
from .forms import UserRegistrationForm, CustomLoginForm
from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy

# Authentication proceeds 
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the login page
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('index')  # Redirect to the home page after login

def logout_view(request):
    logout(request)
    return redirect('login')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = '/password-reset/done/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            # If the email is not registered, render a custom template
            return render(self.request, 'registration/email_not_found.html', {'email': email})
        return super().form_valid(form)


# pages views 
def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = {
        "products":products,
        "category":category
    }
    return render(request, "pages/index.html", context)

def shop(request):
    return render(request, "pages/shop-grid.html")

def blog(request):
    return render(request, "pages/blog.html")

def contact(request):
    return render(request, "pages/contact.html")
