from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^say/$', views.say, name='say'),
    url(r'^sayhello/$', views.sayhello, name='sayhello'),

    # 获取前端向后端请求的参数
    # 获取请求行的数据
    # 未命名参数
    # url(r'^weather/(\w+)/(\d+)/$', views.weather)
    # 命名参数
    url(r'^weather/(?P<city>\w+)/(?P<weather>\d+)/$', views.weather),  # 关键字 指定 传参 -->def weather(request, city, weather )
    # 查询字符串
    url(r'qs/$', views.qs),
    # 获取表单数据
    url(r'get_form/$',views.get_form),
    # 获取非表单数据
    url(r'json_data/$', views.get_json_data),
    # 获取请求头数据
    url(r'header/$', views.get_headers),
    # HttpRspone
    url(r'demo_view/$', views.demo_view),
]