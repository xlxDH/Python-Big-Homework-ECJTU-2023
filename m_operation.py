import tkinter as tk
import tkinter.messagebox as msg
from PIL import ImageTk, Image
import manager
import search
import pymysql
from tkinter import ttk
import idus

def frame():
    global acs
    acs = tk.Tk()
    acs.geometry('800x600')
    acs.title('管理员')
    img = Image.open(r"background.jpg")
    im = ImageTk.PhotoImage(img)
    tk.Label(acs, image=im).pack()

    lable0 = tk.Label(acs, text='欢迎来到睡前消息', font=('微软雅黑', 50)).pack()

    lable1 = tk.Label(acs, text='请选择操作', font=('微软雅黑', 20), fg='GhostWhite', bg='MediumOrchid').place(x=200, y=450)
    tk.Button(acs, text='购进图书', font=('黑体', 15), width=10, height=2, fg='GhostWhite', bg='MediumOrchid', command=purchase).place(x=550, y=300)
    tk.Button(acs, text='注销图书', font=('黑体', 15), width=10, height=2, fg='GhostWhite', bg='MediumOrchid', command=cancel).place(x=550, y=400)
    tk.Button(acs, text='信息查询', font=('黑体', 15), width=10, height=2, fg='GhostWhite', bg='MediumOrchid', command=search.frame).place(x=550, y=500)
    acs.mainloop()

def purchase():
    global acs1
    acs1 = tk.Tk()
    acs1.wm_attributes('-topmost', 1)
    acs1.title('管理员')
    acs1.geometry('800x300')


    comvalue=tk.Label(acs1, text='图书类目：', font=('宋体', 12), ).place(x=30, y=200)
    global list
    list = ttk.Combobox(acs1,textvariable=comvalue,height=10,width=10)
    list.place(x=100,y=200)
    list['values'] = ('全部','人文','艺术','计算机','社科','杂志','自然科学')
    list.current(0)

    global b_name
    tk.Label(acs1, text='书名：', font=('宋体', 12) ).place(x=200, y=200)
    b_name = tk.Entry(acs1,font=('宋体',12),width=10)
    b_name.place(x=250,y=200)

    global author
    tk.Label(acs1, text='作者：', font=('宋体', 12) ).place(x=350, y=200)
    author = tk.Entry(acs1, font=('宋体', 12), width=10)
    author.place(x=400, y=200)

    global publishing
    tk.Label(acs1, text='出版社：', font=('宋体', 12) ).place(x=450, y=200)
    publishing = tk.Entry(acs1, font=('宋体', 12), width=10)
    publishing.place(x=500, y=200)

    global amount
    tk.Label(acs1, text='数量：', font=('宋体', 12) ).place(x=560, y=200)
    amount = tk.Entry(acs1, font=('宋体', 12), width=5)
    amount.place(x=610, y=200)

    tk.Button(acs1, text='确认添加', font=('黑体', 12), width=10, height=2, command=add).place(x=700, y=195)

def add():
    sql='INSERT INTO book(name,type,publishing,author,amount) VALUES(%s,%s,%s,%s,%s)'
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='acs',
        password='123',
        db='library',
        charset='utf8'
    )
    cusor = db.cursor()
    cusor.execute(sql,(b_name.get(),list.get(),publishing.get(),author.get(),amount.get()))
    db.commit()
    db.close()
    msg.showinfo(title='成功！',message='新书已入库！')

def cancel():
    global acs1
    acs1 = tk.Tk()
    acs1.wm_attributes('-topmost', 1)
    acs1.title('管理员')
    acs1.geometry('800x300')

    comvalue=tk.Label(acs1, text='图书类目：', font=('宋体', 12) ).place(x=30, y=200)
    global list
    list = ttk.Combobox(acs1, textvariable=comvalue, height=10, width=10)
    list.place(x=100, y=200)
    list['values'] = ('全部', '人文', '艺术', '计算机', '社科', '杂志', '自然科学')
    list.current(0)

    global b_name
    tk.Label(acs1, text='书名：', font=('宋体', 12) ).place(x=200, y=200)
    b_name = tk.Entry(acs1, font=('宋体', 12), width=10)
    b_name.place(x=250, y=200)

    global author
    tk.Label(acs1, text='作者：', font=('宋体', 12) ).place(x=350, y=200)
    author = tk.Entry(acs1, font=('宋体', 12), width=10)
    author.place(x=400, y=200)

    global publishing
    tk.Label(acs1, text='出版社：', font=('宋体', 12) ).place(x=460, y=200)
    publishing = tk.Entry(acs1, font=('宋体', 12), width=10)
    publishing.place(x=510, y=200)

    global amount
    tk.Label(acs1, text='数量：', font=('宋体', 12) ).place(x=570, y=200)
    amount = tk.Entry(acs1, font=('宋体', 12), width=5)
    amount.place(x=620, y=200)

    tk.Button(acs1, text='确认注销', font=('黑体', 12), width=10, height=2 , command = remove1).place(x=700, y=195)

def remove1():
    sql = 'DELETE FROM book WHERE type=%s AND name=%s AND author=%s'
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='acs',
        password='123',
        db='library',
        charset='utf8'
    )
    cursor = db.cursor()
    result = cursor.execute(sql,(list.get(), b_name.get(), author.get()))
    if result:
        db.commit()
        msg.showinfo(title='成功！', message='该书已删除！')
    else:
        msg.showinfo(title='失败！', message='该书未删除！')
        db.rollback()
    cursor.close()
    db.close()
