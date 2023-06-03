from django.shortcuts import render, redirect
from django import forms
from dataPage import models


# Create your views here.
def index(request):
    return render(request, 'index.html')

class UserModelForm(forms.ModelForm):
    class meta:
        model = models.UserInfo
        fields = ['username', 'password', 'age', 'account', 'create_time', 'depart', 'gender']


def user_index(request):
    return render(request, 'user_index.html')


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            print(name, field)
            if name == 'password':
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label, 'type': 'password'}
                continue
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

def user_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/index/')
    return render(request, 'user_add.html', {'form': form})

def user_info(request):
    return render(request, 'user_info.html')


def user_edit(request):
    return render(request, 'user_edit.html')

def user_delete(request):
    return render(request, 'user_index.html')


class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ['title']

    # wigets = {
    #     'title':forms.TextInput(attrs={'class':'form-control'})
    # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name,field)
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def department_add(request):
    if request.method == 'GET':
        form = DepartmentModelForm()
        return render(request, 'department_add.html', {'form': form})
    form = DepartmentModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/department/info/')
    return render(request, 'department_add.html', {'form': form})


def department_index(request):
    query_list = models.Department.objects.all().order_by('id')
    for item in query_list:
        print(item.id, item.title)
    return render(request, 'department_index.html', {'query_list': query_list})


def department_edit(request):
    return render(request, 'department_edit.html')

def department_delete(request):
    return render(request, 'department_index.html')