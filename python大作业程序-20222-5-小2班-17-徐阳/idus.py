import tkinter as tk
import tkinter.messagebox as msg
import pymysql
import init
import manager
import reader
import m_operation
import r_operation
def id_check(a):#检查账号
    global username
    if a == '1':#在管理员界面下登录，参数是1
        username = manager.entry_name.get()
        password = manager.entry_key.get()
    elif a == '0':#在读者界面下登录，参数是0
        username = reader.entry_name.get()
        password = reader.entry_key.get()
    # get_username()

    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='acs',
        password='123',
        db='library',
        charset='utf8'
    )
    #建立游标cursor，这个游标可以类比指针，这样理解比较直观
    cursor = db.cursor()
    sql = "SELECT password FROM userinfo WHERE username=%s AND job=%s"
    cursor.execute(sql,(username,a)) #sql语8句被执行
    result = cursor.fetchone()#得到的结果返回给result数组
    if result:#如果查询到了账号存在
            if password == result[0]:#result[0]是数组中的第一个结果
                success_login(a)#密码对上了，进入对应的读者/管理员操作界面
            else:#有账号但密码没对上
               msg._show(title='错误！',message='账号或密码输入错误！')
    else:#没有账号
        msg._show(title='错误！',message='您输入的用户不存在！请先注册！')
        if a=='1':
            manager.root1.destroy()#关闭登录小窗口，回到管理员界面
        elif a=='0':
            reader.root1.destroy()
    db.close()#查询完一定要关闭数据库啊

def success_login(a):#成功登录
    if a == '1':
        manager.root1.destroy()
        m_operation.frame()#销毁登录注册界面，跳转到管理员的操作界面

    elif a == '0':
        reader.root1.destroy()
        r_operation.frame()#销毁登录注册界面，跳转到读者的操作界面

def id_write(a):#写入（注册）账号
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='acs',
        password='123',
        db='library',
        charset='utf8'
    )
    cursor = db.cursor()
    if a== '1':#跟check函数里边十分类似
        username = manager.entry_name.get()#得到输入的账号
        password = manager.entry_key.get()#得到输入的密码
        confirm = manager.entry_confirm.get()#得到输入的确认密码
    elif a== '0':
        username = reader.entry_name.get()
        password = reader.entry_key.get()
        confirm = reader.entry_confirm.get()

    sql0 = 'SELECT id FROM userinfo WHERE username=%s AND job=%s'
    sql1 = 'INSERT INTO userinfo(username,password,job) values(%s,%s,%s)'
#首先检查两次输入的密码是否一致，一致后再检查注册的账号是否已经存在
    if password == confirm:
        result = cursor.execute(sql0,(username,a))
        if result:
            msg.showerror(title='错误！', message='该账号已被注册，请重新输入！')
        else:
            cursor.execute(sql1,(username,password,a))
            db.commit()
            db.close()
            msg.showinfo(title='成功！', message='注册成功，请登录！')

    else:
        msg.showerror(title='错误！', message='两次密码不一致，请重新输入！')

def get_username():
    return username
