from django.shortcuts import render,redirect,HttpResponse
from app02 import models
# Create your views here.
def depart_list(req):
    '''部门列表'''
    data_list = models.Department.objects.all()
    return render(req,'depart_list.html',{'data_list': data_list})

def depart_add(req):
    '''添加部门'''
    if req.method == 'GET':
        return render(req,'depart_add.html')
    else:
        title = req.POST.get('title')
        models.Department.objects.create(title=title)
        return redirect('/depart/list')

def depart_del(req):
    id = req.GET.get('id')
    models.Department.objects.filter(id=id).delete()
    return redirect('/depart/list')

def depart_update(req,nid):
    if req.method == 'POST':
        title = req.POST.get('title')
        models.Department.objects.filter(id=nid).update(title=title)
        return redirect('/depart/list')

def depart_edit(req,nid):
    if req.method == 'GET':
        data_list = models.Department.objects.filter(id=nid).first()
        return render(req,'depart_edit.html',{'data_list': data_list})
    title = req.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/list')

def layout(req):
    return render(req,'extend_layout.html')

# ------------------ 用户管理 -------------------
def user_list(req):
    data_list = models.UserInfo.objects.all()
    return render(req,'app02user_list.html',{'data_list':data_list})

def user_add(req):
    if req.method == 'GET':
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart': models.Department.objects.all()
        }
        return render(req,'user_add.html',context)
    if req.method == 'POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        password = req.POST.get('password')
        gender = req.POST.get('gender')
        create_time = req.POST.get('create_time')
        account = req.POST.get('account')
        depart_id = req.POST.get('depart_id')
        models.UserInfo.objects.create(name=name,age=age,password=password,gender=gender,create_time=create_time,account=account,depart_id=depart_id)
        return redirect('/user/list')

# --------------- ModelForm -----------------
from django import forms
class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name','password','age','account','create_time','gender','depart']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name, field in self.fields.items():
            print("field:---",field)
            field.widget.attrs = {'class': 'form-control'}

def user_model_add(req):
    if req.method == 'GET':
        form = UserModelForm()
        return render(req,'user_add.html',{'form':form})
    # 提交数据校验
    form = UserModelForm(data=req.POST)
    if form.is_valid():
       # print(form.cleaned_data) # 得到用户输入的正确数据 {'name':'123,'age':11,....}
        form.save() # 保存数据到数据库
        return redirect('/user/list')
    else:
        return render(req,'user_add.html',{'form':form})


def user_edit(req,nid):
    if req.method == 'GET':
        data_list = models.UserInfo.objects.filter(id=nid).first()
        return render(req,'user_edit.html',{'data_list':data_list})
    if req.method == 'POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        password = req.POST.get('password')
        gender = req.POST.get('gender')
        create_time = req.POST.get('create_time')
        account = req.POST.get('account')
        depart_id = req.POST.get('depart_id')
        models.UserInfo.objects.filter(id=nid).update(name=name,age=age,password=password,gender=gender,create_time=create_time,account=account,depart_id=depart_id)
        return redirect('/user/list')

def user_delete(req):
    id = req.GET.get('id')
    models.UserInfo.objects.filter(id=id).delete()
    return redirect('/user/list')
