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