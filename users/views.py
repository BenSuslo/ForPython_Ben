from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """注销用户"""
    # 函数logout()要求将request对象作为实参，然后重定向到主页
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        # 默认表单UserCreationForm
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        # 检查这些数据是否有效：就这里而言，是用户名未包含非法字符，输入的两个密码相同，以及用户没有试图做恶意的事情
        if form.is_valid():
            # 调用表单的方法save()，将用户名和密码的散列值保存到数据库中，返回新创建的用户对象
            new_user = form.save()
            # 让用户自动登录，在重定向到主页
            # 调用authenticate()，并将实参new_user.username和密码传递给它
            # 用户注册时，被要求输入密码两次；由于表单是有效的，我们知道输入的这两个密码是相同的，因此可以使用其中任何一个
            # 如果用户名和密码无误，方法authenticate()将返回一个通过了身份验证的用户对象
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)