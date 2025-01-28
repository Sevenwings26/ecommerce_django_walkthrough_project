from django.shortcuts import render
from .models import User, Product, Order, OrderItem
from products.models import Product, Category
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordResetView
from .forms import UserRegistrationForm, CustomLoginForm
from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy
# from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse


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
        "category":category,
    }
    return render(request, "pages/index.html", context)




def add_to_cart(request, product_id):
    """
    Add to cart
    """
    product = get_object_or_404(Product, id=product_id)
    user = request.user if request.user.is_authenticated else None
    
    order, created = Order.objects.get_or_create(customer=user, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()

    return redirect(request.META.get('HTTP_REFERER', 'home'))


# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     user = request.user if request.user.is_authenticated else None
#     order, created = Order.objects.get_or_create(customer=user, complete=False)

#     order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
#     order_item.quantity += 1
#     order_item.save()

#     # If AJAX request, return JSON response
#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         return JsonResponse({
#             'cart_items': order.get_cart_items,
#             'cart_total': order.get_cart_total,
#         })
#     return redirect(request.META.get('HTTP_REFERER', 'home'))


def remove_from_cart(request, pk):
    user = request.user
    order = Order.objects.filter(customer=user, complete=False).first()
    if order:
        order_item = get_object_or_404(OrderItem, pk=pk, order=order)
        order_item.delete()
    return redirect('cart')  # Redirect to the checkout page or cart page


def cart(request):
    user = request.user if request.user.is_authenticated else None
    order = Order.objects.filter(customer=user, complete=False).first()
    items = order.orderitem_set.all() if order else []

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'pages/cart.html', context)

# views.py
import uuid
from django.shortcuts import render, redirect
from django.conf import settings
from paystackapi.transaction import Transaction

def checkout(request):
    order = Order.objects.filter(customer=request.user, complete=False).first()
    if request.method == "POST":
        transaction_ref = str(uuid.uuid4())  # Generate a unique transaction reference
        amount = int(order.get_cart_total * 100)  # Amount in kobo/cents

        # Pass transaction data to Paystack
        response = Transaction.initialize(
            reference=transaction_ref,
            email=request.user.email,
            amount=amount,
            callback_url=request.build_absolute_uri('/verify-payment/'),
        )
        return redirect(response['data']['authorization_url'])  # Redirect to Paystack

    items = order.orderitem_set.all()
    context = {
        'items': items,
        'order': order,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
    }
    return render(request, 'checkout.html', context)


from django.http import JsonResponse
from paystackapi.transaction import Transaction

def verify_payment(request):
    reference = request.GET.get('reference')
    response = Transaction.verify(reference=reference)
    if response['status'] == True:
        # Update the order to complete
        order = Order.objects.get(transaction_id=reference)
        order.complete = True
        order.save()

        return JsonResponse({'status': 'success', 'message': 'Payment successful!'})
    return JsonResponse({'status': 'failure', 'message': 'Payment failed. Please try again.'})



def shop(request):
    return render(request, "pages/shop-grid.html")

def blog(request):
    return render(request, "pages/blog.html")

def contact(request):
    return render(request, "pages/contact.html")


