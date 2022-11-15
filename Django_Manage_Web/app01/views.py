from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('欢迎来到Django的世界，Hello World！')

def user_list(request):
    # 根据app的注册顺序，逐一去他们的templates目录中找
    # 并不是只是在它自己的templates中找user_list.html
    name = "学生"
    role = ['班长','团支书','心理委员']
    return render(request,'user_list.html',{"name": name,"r": role})

def connect_data(req):

    import requests
    res = requests.get('http://www.baidu.com') # 写一个有效的接口地址
    data = res.json()
    print(data)

    # req是一个对象，封装了用户发送来的所有请求相关的数据
    # 1.获取请求方式 GET/POST
    print(req.method)

    # 2.在URL上传递值 /admin/data/?n1=12&b1=34
    print(req.GET)

    # 3.在请求体中提交数据
    print(req.POST)

    return render(req,'user_list.html',{"data": data})

def connect_mysql(req):
    import pymysql
    # 1.连接Mysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root123', charset='utf8', db='unicom')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 2.发送指令
    cursor.execute("insert into admin(username,password,mobile) values('suyufan','123','122')")
    conn.commit()
    # 3.关闭
    cursor.close()
    conn.close()

def login(req):
    if req.method == 'GET':
        return render(req,'user_login.html')
    else:
        print(req.POST)
        username = req.POST.get('username')
        pwd = req.POST.get('password')
        return HttpResponse('登录成功')

from app01.models import Department
def orm(req):
    # 1.增加数据 insert into app01_department(title) values('销售部')
    Department.objects.create(title="数据库产品中心")

    # 2.删除数据
    Department.objects.filter(id=1).delete()  # 删掉id为1的一行
    Department.objects.all().delete() # 删除Department中的所有数据

    # 3.查询数据
    # data_list = [对象，行，行]  QuerySet类型
    data_list = Department.objects.all()
    for obj in data_list:
        print(obj.title)
    # 只取第一行 可以 Department.objects.filter(id=1).first()

    # 4.更新数据
    Department.objects.filter(id=1).update(title="CVM产品中心")

    return HttpResponse('成功')
