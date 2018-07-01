from django.conf.urls import url

from . import views

urlpatterns = [
    # 定义路由的视图函数
    url(r'index/', views.index),
    url(r'show/$',views.show_books)
]