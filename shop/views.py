from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import  Product, Address, Users
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

# Create your views here.
def index(request):
    product_objs = Product.objects.all()

    query = request.GET.get("item_name")
    print("********", query)
    if query:
        product_objs = Product.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    paginator = Paginator(product_objs, 4) # 4  per page
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj
    }

    # paginator = Paginator(product_objs, 4) # Show 25 contacts per page.
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request, 'shop/index.html', context)

    # return render(request, 'shop/index.html', {'products':product_objs})


def detail(request, id):
    product_obj = Product.objects.get(id = id)
    context = {
        'product': product_obj
    }
    return render(request, 'shop/detail.html', context)

def checkout(request):

    return render(request, 'shop/checkout.html')

def place_order(request):
    if request.method == 'POST':
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        price = request.POST.get("price")
        products = request.POST.get("products")
        # print("***products",products)
        add_items = Address(item=products,firstname=first_name, lastname=last_name,address=address,email=email,phone=phone,total_price=price)
        add_items.save()

        from django.contrib import messages
        messages.info(request,"Order Placed!")  # nothing is showed
        return redirect("index")

def register(request):
    return render(request, 'shop/register.html')

def sign_in(request):
    return render(request, 'shop/signin.html')

def sign_out(request):
    logout(request)
    return redirect("index")

def change_pass_page(request):
    return render(request, 'shop/change_password.html')

def change_password_action(request):
    if request.method == 'POST':
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        # allow = request.POST.get("allow")

        from django.contrib.auth import authenticate

        password = request.POST.get("password")
        print(f"password:{password}")
        repeat_password = request.POST.get("repeat_password")

        context = {'username':user_name,
                   'email':email,
                   }
        if not user_name or not email:
            context['message'] = "Please enter user name or email!"
            return render(request, 'shop/register.html', context)
        if password != repeat_password:
            context['message'] = "Passwords are different!"
            return render(request, 'shop/register.html', context)
        # if not allow:
        #     context['message'] = "Please check agreement!"
        #     return render(request,'shop/register.html', context)context

        try:
            user = Users.objects.get(username=user_name,email=email)
        except Users.DoesNotExist:
            user = None
        if not user:
            context['message'] = "User Name or Email Is Wrong!"
            return render(request, 'shop/change_password.html', context)

        user.set_password(password)
        user.is_active = True
        user.save()
        # send active email to user asychronize so the page can be return directely

    return redirect("index")

def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        allow = request.POST.get("allow")

        print("+++++",allow)

        from django.contrib.auth import authenticate

        password = request.POST.get("password")
        # print(f"password:{password}")
        repeat_password = request.POST.get("repeat_password")

        context = {'username':user_name,
                   'email':email,
                   }
        if not user_name or not email:
            context['message'] = "Please enter user name or email!"
            return render(request, 'shop/register.html', context)
        if password != repeat_password:
            context['message'] = "Passwords are different!"
            return render(request, 'shop/register.html', context)
        if not allow:
            context['message'] = "Please check agreement!"
            return render(request,'shop/register.html', context)

        try:
            user = Users.objects.get(username=user_name)
        except Users.DoesNotExist:
            user = None
        if user:
            context['message'] = "User existed!"
            return render(request, 'shop/register.html', context)


        items = Users.objects.create_user(username=user_name, email=email, password=password, is_active=True, create_time=datetime.now(), last_modify_time=datetime.now())
        items.save()
        # send active email to user asychronize so the page can be return directely

    return redirect("index")


def sign_in_login(request):
    # user_name = request.POST.get("user_name")
    # password = request.POST.get("password")
    user_name = request.POST['user_name']
    password = request.POST['password']
    if not user_name or not password:
        return render(request,'shop/signin.html',{'message':'Please input user email and password'})
    user = authenticate(request, username=user_name, password=password)
    print("user---", user)
    if user is not None:
        login(request, user)
        print("user log in*****")
        return redirect("index")
    else:
        return render(request,'shop/signin.html',{'message':'Please Sign up!'})


