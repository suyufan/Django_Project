import json
from django import forms
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # 免除csrf_token验证 加上之后 可以通过Ajax发送post请求 不会403禁止访问

from app02 import models
from app02.utils.bootstrap import BootStrapModelForm


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            # "detail": forms.Textarea,
            "detail": forms.TextInput
        }


def task_list(request):
    """ 任务列表 """
    form = TaskModelForm()
    return render(request, "task_list.html", {"form": form})


@csrf_exempt # post请求免除校验
def task_ajax(request):
    print(request.GET)
    print(request.POST)

    data_dict = {"status": True, 'data': [11, 22, 33, 44]}
    return HttpResponse(json.dumps(data_dict))


@csrf_exempt
def task_add(request):
    # {'level': ['1'], 'title': ['sdfsdfsdfsd'], 'detail': ['111'], 'user': ['8']}
    # print(request.POST)

    # 1.用户发送过来的数据进行校验（ModelForm进行校验）
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))

    # return JsonResponse(data_dict)
