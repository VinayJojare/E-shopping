import include
from django.http import HttpResponse
from django.urls import path, include
from store.views.home import Index
from store.views.signup_view import Signup
from store.views.login_view import Login, logout
from django.conf import settings
from django.conf.urls.static import static
from store.views.orders import Orders

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('order', Orders.as_view(), name='order'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
