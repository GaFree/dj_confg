from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseBadRequest,JsonResponse
from django.urls import reverse
import json


# Create your views here.
def say(request):
    url = reverse('reqresp:sayhello')
    print(url)
    return HttpResponse('say!!!')


def sayhello(request):
    # url = reverse('reqresp:say')
    # print(url)
    return redirect(reverse('reqresp:say'))  # redirect 重定向-->> /say
    # return HttpResponse('sayhello!!!')


# 获取前端向后端请求的参数
# 请求行的数据
# http：//www.baidu.com/weather/sz
# 未命名参数
def weather(request, city, weather):
    print(weather)
    print(city)
    return HttpResponse('ok!!')


# 查询字符串
# 使用 querydict
# get 获取单个数据，如果key的有多个值，获最后一个值
# getlist 获取全部值
def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    a_list = request.GET.getlist('a')
    print(a)
    print(b)
    print(a_list)
    return HttpResponse('ok!')


def get_form(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    a_list = request.POST.getlist('a')
    print(a)
    print(b)
    print(a_list)
    return HttpResponse('ok!')


# 获取非表单
def get_json_data(request):
    # 获取数据
    body_data = request.body
    print(type(body_data))
    # 转码，转化为string
    json_data = body_data.decode()  # py 3.6 自动转换 不用此操作
    print(json_data)
    print(type(json_data))
    # 把string 转化为dict
    data = json.loads(json_data)
    print(type(data))
    # 输出
    print(data['a'])
    return HttpResponse('ok')


# 获取请求体数据
def get_headers(request):
    print(request.META)
    print(request.path)  # 获取路由完整路径
    return HttpResponse('OK!!!')


# HttpResponse
# def demo_view(request):
#     # return HttpResponse('itcast python', status = HttpResponseBadRequest)  # Django提供了一系列HttpResponse的子类，可以快速设置状态码
#
#     # 动态添加响应内容
#     resp = HttpResponse()
#     resp['itcast'] = 'python'
#     resp['status'] = '302'
#     return resp

# json 数据
def demo_view(request):
    # return JsonResponse({'city': 'beijing','subject': 'python'})
    return HttpResponse(content={'city': 'beijing', 'subject': 'python'}, content_type='application/json')