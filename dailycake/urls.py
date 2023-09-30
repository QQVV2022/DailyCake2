"""dailycake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/
    from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('placeorder', views.place_order, name='placeorder'),
    path('register/', views.register, name='register'),
    path('signup', views.sign_up, name='signup'),
    path('signout', views.sign_out, name='signout'),
    path('signin_login', views.sign_in_login, name='signinlogin'),
    path('signin', views.sign_in, name='signin'),
    path('changepasspage', views.change_pass_page, name='changepasspage'),
    path('changepassword', views.change_password_action, name='changepassword'),
]
