from django.shortcuts import render, redirect, HttpResponse
from app01 import models
import datetime


# Create your views here.
def tpl(request):
    import requests
    name = '刘俊'
    role = ['管理员', '普通用户']
    dict = {'name': '张三', 'age': '21'}
    date_lst = [{'name': '张三', 'age': '21'}, {'name': '李四', 'age': '22'}]
    url = 'http://www.chinaunicom.com.cn/api/article/NewsByIndex/1/2023/05/news'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36'
    }
    data_list = requests.get(url, headers=headers).json()

    return render(request, 'tpl.html', {"n1": name, "n2": role, "n3": dict, "n4": date_lst, 'data_list': data_list})


def request(request):
    method = request.method
    if method == 'GET':
        args = request.GET.dict()
        return render(request, 'request.html', {'n1': method, 'n2': args})
    else:
        args = request.POST.dict()
        return render(request, 'request.html', {'n1': method, 'n2': args})


def res_redirect(request):
    return redirect('https://www.opcloud.cn/')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == models.Userinfo.objects.get(username=username).username and password == models.Userinfo.objects.get(username=username).password:
        return redirect('/index/')
    return redirect('/login/')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    fullname = request.POST.get('fullname')
    age = request.POST.get('age')
    print(request.POST.get('join_time'))
    join_time = datetime.datetime.strptime(request.POST.get('join_time'), '%Y/%m/%d').date()
    models.Userinfo.objects.create(username=username, password=password, fullname=fullname, age=age, join_time=join_time)
    return redirect('/login/')

def index(request):
    return render(request, 'user_index.html')

def department(request):
    return render(request, 'department.html')

class MyForm(Form):
    user = forms.CharField(wiget=forms.Input)
    pwd = forms.CharField(wiget=forms.Input)
def user_add(request):
    return render(request, 'user_add.html', {'form': MyForm()})