from django.shortcuts import render
from products.models import Product, Category
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm, CustomLoginForm
from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy


# Sign-up view
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
