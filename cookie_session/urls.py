from django.conf.urls import url

from cookie_session.views import my_decorator
from . import views

urlpatterns = [
    url(r'cs/$', views.cookie_session),
    # 中间件
    url(r'demo/$', views.demo_view),
    # 视图函数
    # url(r'reg/$', views.register),
    # url(r'reg/$', my_decorator(views.RegistView.as_view())),
    url(r'reg/$', views.RegistView.as_view()),
    # mixin 扩展类
    url(r'booksview/$', views.BooksView.as_view()),
    #
    url(r'tem/$', views.index)
]