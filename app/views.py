from django.shortcuts import render, redirect
from django.views import View
from rbac.service.init_permission import init_permission
from rbac import models
from app.utils import getmd5


class AuthView(object):
    """
    session 验证,session中没有用户名，返回登陆
    """

    # 路由后触发类执行时dispatch方法会优先被执行
    def dispatch(self, request, *args, **kwargs):
        if request.session.get('userinfo'):
            response = super(AuthView, self).dispatch(request, *args, **kwargs)
            # 返回 View类中映射的get/post方法
            return response
        else:
            return redirect("login")


class LoginView(View):
    """"
    登陆
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(" {0}登陆 ".format(username).center(50, '*'))
        password = getmd5.md5(password)
        obj = models.User.objects.filter(username=username, password=password).first()
        if obj:
            # 初始化用户session信息
            init_permission(request, obj)
            request.session['userinfo'] = {'username': obj.username, 'is_login': True}
            return redirect("index")
        return render(request, 'login.html', {'msg': '用户名或密码错误!'})


class LogoutView(View):
    """
    退出
    """

    def get(self, request, *args, **kwargs):
        username = request.session.get('userinfo')['username']
        print(" {0}退出 ".format(username).center(50, '*'))
        request.session.clear()
        return redirect('login')


class IndexView(AuthView, View):
    """
    首页
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class HostListView(AuthView, View):
    """
    主机列表
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'host.html')


class HostAddView(AuthView, View):
    """
    主机添加
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'host_add.html')


class UserInfoView(AuthView, View):
    """
    用户列表
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'user.html')


class UserAddView(AuthView, View):
    """
    用户添加
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'user_add.html')
