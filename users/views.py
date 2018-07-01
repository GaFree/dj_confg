from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo

# Create your views here.
def index(request):
    """
    定义视图函数
    :param request: 形参，接受前端发来的请求
    :return:
    """
    return HttpResponse("Hello Python !!!")


def show_books(request):
    """模板展示数据"""
    # context = {
    #     'name': '隔壁老王'
    # }
    # list_a = ['东邪', '西毒', '1', '2', '3']
    # content = {'list_a': list_a}

    # 查询数据库
    # 组装数据, books  是查询集
    # BookInfo.objects.all() 拿到数据库的所有数据
    books = BookInfo.objects.all()
    content = {'books': books}
    return render(request, 'index.html', context=content)
