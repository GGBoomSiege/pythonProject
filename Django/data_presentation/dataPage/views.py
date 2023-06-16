from django.shortcuts import render, redirect
from django import forms
from dataPage import models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_index(request):
    user_info = models.UserInfo.objects.all().order_by('create_time')
    user_head = models.UserInfo._meta.fields
    for item in user_info:
        item.create_time = item.create_time.strftime('%Y-%m-%d')
        # print(item.create_time)
    return render(request, 'user_index.html', {'user_head': user_head, 'user_info': user_info})


class UserAddForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ('username', 'password', 'age', 'account', 'depart', 'gender', 'create_time',)

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'account': forms.NumberInput(attrs={'class': 'form-control'}),
            'depart': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'create_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

def user_add(request):
    if request.method == 'GET':
        form = UserAddForm()
        return render(request, 'user_add.html', {'form': form})
    form = UserAddForm(data=request.POST)
    # print(request.POST.get('create_time'))
    if form.is_valid():
        form.save()
        return redirect('/user/index/')
    return render(request, 'user_add.html', {'form': form})


def user_info(request):
    return render(request, 'user_info.html')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ('username', 'age', 'account', 'depart', 'gender', 'create_time',)

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'account': forms.NumberInput(attrs={'class': 'form-control'}),
            'depart': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'create_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

def user_edit(request, nid):
    userData = models.UserInfo.objects.get(id=nid)
    if request.method == 'GET':
        form = UserEditForm()
        userData.create_time = userData.create_time.strftime('%Y-%m-%d');
        return render(request, 'user_edit.html', {'form': form, 'data': userData})
    form = UserEditForm(instance=userData,data=request.POST)
    print(request.POST.get('username'))
    if form.is_valid():
        form.save()
        return redirect('/user/index/')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    userData = models.UserInfo.objects.get(id=nid)
    userData.delete()
    return redirect('/user/index/')


class DepartmentAddForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for name, field in self.fields.items():
    #         # print(name,field)
    #         field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def department_add(request):
    if request.method == 'GET':
        form = DepartmentAddForm()
        return render(request, 'department_add.html', {'form': form})
    form = DepartmentAddForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/department/index/')
    return render(request, 'department_add.html', {'form': form})


def department_index(request):
    query_list = models.Department.objects.all().order_by('title')
    # for item in query_list:
    #     print(item.id, item.title)
    return render(request, 'department_index.html', {'query_list': query_list})

class DepartmentEditForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }

def department_edit(request, nid):
    departmentData = models.Department.objects.get(id=nid)
    if request.method == 'GET':
        form = DepartmentEditForm(instance=departmentData)
        return render(request, 'department_edit.html', {'form': form, 'data': departmentData})
    form = DepartmentEditForm(instance=departmentData, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/department/index/')
    return render(request, 'department_edit.html', {'form': form})


def department_delete(request, nid):
    departmentData = models.Department.objects.get(id=nid)
    departmentData.delete()
    return redirect('/department/index/')

def getJob_index(request):
    if request.method == 'GET':
        return render(request, 'getjob_index.html')

    return render(request, 'getjob_index.html')
