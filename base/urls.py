from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('send_email/', views.sendEmail, name="send_email"),
]