from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator  # django自带的类视图装饰器
from django.template import loader

# Create your views here.
def cookie_session(request):
    # 设置session
    request.session['itcast'] = 'python'
    # 读取session
    session = request.session.get('itcast')
    print(session)
    return HttpResponse('天王盖地虎！')


# 视图函数
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        return HttpResponse('这是一个 post请求')






# 自定义装饰器
# 需求：给类视图的请求方法加装饰器
def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        # def wrapper(self,request, *args, **kwargs):    添加 self 能直接给类里面的函数直接添加装饰器
        print("自定义装饰器被调用了")
        print("请求路径%s" % request.path)
        # return func(self,request, *args, **kwargs)   添加 self 能直接给类里面的方法直接添加装饰器
        return func(request, *args, **kwargs)

    return wrapper


# 视图
# 给类视图的请求方法加装饰器
@method_decorator(my_decorator, name='dispatch')  # “ dispatch ”是 as_view() 的 name  每个类方法都添加装饰器
# @method_decorator(my_decorator, name='get')
class RegistView(View):
    """类视图"""

    # @method_decorator(my_decorator)
    # @my_decorator
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        return HttpResponse('这是post 请求！！')

    # @method_decorator(my_decorator)
    # @my_decorator
    def put(self, request):
        return HttpResponse('这是put 请求！！')


# mixin 扩展类
class ListModelMixin(object):
    """
    list 扩展类
    """

    def list(self, request, *args, **kwargs):
        print("是list")


class CreateModelMixin(object):
    """
    create 扩展类
    """

    def create(self, request, *args, **kwargs):
        print("是create")


class BooksView(CreateModelMixin, ListModelMixin, View):
    """
    同时继承两个扩展类，复用list和create方法
    """

    def get(self, request):
        self.list(request)
        return HttpResponse("天王盖地虎‘get’")

    def post(self, request):
        self.create(request)
        return HttpResponse("小鸡炖蘑菇‘post’")

# 中间件
def demo_view(request):
    print('view 视图被调用')
    return HttpResponse('OK')

# 模板加载的原理
def index(request):
    # 1,获取模板
    # template = loader.get_template('index.html')

    context = {'city': '北京'}
    # 2, 渲染模板
    # return HttpResponse(template.render(context))
    return render(request, 'index.html', context)