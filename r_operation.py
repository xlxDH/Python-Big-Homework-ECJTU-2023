import  tkinter as tk
import  tkinter.messagebox as msg
from PIL import ImageTk, Image
import reader
import search
import pymysql
from tkinter import  ttk
import idus
import datetime as dt#datetime

def frame():
    global acs
    acs = tk.Tk()
    acs.geometry('800x600')
    acs.title('读者')
    img=Image.open(r"background.jpg")
    im = ImageTk.PhotoImage(img)
    tk.Label(acs,image=im).pack()


    lable0 = tk.Label(acs, text='欢迎来到睡前消息', font=('微软雅黑', 50), fg='GhostWhite', bg='MediumOrchid' ).pack()

    lable1 = tk.Label(acs, text='请选择操作', font=('微软雅黑', 20), fg='GhostWhite', bg='MediumOrchid' ).place(x=200, y=450)
    tk.Button(acs, text=' 借 书', font=('黑体', 15), width=10, height=2 , fg='GhostWhite', bg='MediumOrchid', command=borrow).place(x=550, y=300)
    tk.Button(acs, text=' 还 书', font=('黑体', 15), width=10, height=2 , fg='GhostWhite', bg='MediumOrchid', command=turnback).place(x=550, y=400)
    tk.Button(acs, text='信息查询', font=('黑体', 15), width=10, height=2, fg='GhostWhite', bg='MediumOrchid', command=search.frame).place(x=550, y=500)
    acs.mainloop()

def borrow():
    global acs1
    acs1 = tk.Tk()
    acs1.title('读者')
    acs1.geometry('800x300')
    acs1.wm_attributes('-topmost', 1)


    tk.Label(acs1, text='请填写所借图书的信息:(书名作者都要填写正确无误！)', font=('宋体', 12)).place(x=30, y=100)

    global b_name
    tk.Label(acs1, text='书名：', font=('宋体', 12)).place(x=200, y=200)
    b_name = tk.Entry(acs1, font=('宋体', 12), width=10)
    b_name.place(x=250, y=200)

    global author
    tk.Label(acs1, text='作者：', font=('宋体', 12)).place(x=350, y=200)
    author = tk.Entry(acs1, font=('宋体', 12), width=10)
    author.place(x=400, y=200)

    tk.Button(acs1, text='确认借书', font=('宋体', 12), width=10, command=confirm_borrow).place(x=600, y=195)

def confirm_borrow():
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='acs',
        password='123',
        db='library',
        charset='utf8'
    )
    cursor = db.cursor()
    sql0 = 'SELECT amount FROM book WHERE name=%s AND author=%s'
    cursor.execute(sql0,(b_name.get(), author.get()))
    result = cursor.fetchone()
    if result:
        if result != '0':
            time = dt.datetime.now().strftime('%F')  # 得到的时间不是字符串型，我们要把时间转化成字符串型
            sql = 'INSERT INTO borrow(username,bookname,author,date) VALUES(%s,%s,%s,%s)'
            sql1 = 'UPDATE book SET amount=amount-1 WHERE name=%s AND author=%s'
            cursor.execute(sql,(idus.get_username(), b_name.get(), author.get(), time))
            cursor.execute(sql1,(b_name.get(), author.get()))
            db.commit()
            db.close()
            msg.showinfo(title='成功！', message='借书成功！请一个月之内归还')
        else:
            msg.showinfo(title='失败！', message='您借的书库存不足！')
    else:
        msg.showinfo(title='错误！', message='未找到该书！')

def turnback():
    global acs1
    acs1 = tk.Tk()
    acs1.title('读者')
    acs1.geometry('550x600')

    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='acs',
        password='123',
        db='library',
        charset='utf8'
    )
    cursor = db.cursor()
    sql0 = 'SELECT COUNT(*) FROM borrow WHERE username=%s'
    cursor.execute(sql0,(idus.get_username()))
    result = cursor.fetchone()
    if result[0]==0:
        msg.showinfo(title='错误', message='您还没借过书呢！')
    else :
        lable1 = tk.Label(acs1, text='查询到您有以下书目未还：', font=('微软雅黑', 20)).place(x=80, y=20)
        tree = ttk.Treeview(acs1, columns=('1', '2'), show="headings")
        tree.column('1', width=150, anchor='center')
        tree.column('2', width=150, anchor='center')
        tree.heading('1', text='书名')
        tree.heading('2', text='作者')
        tree.place(x=100, y=100)

        sql1 = 'SELECT bookname,author FROM borrow WHERE username=%s'
        cursor.execute(sql1,(idus.get_username()))
        result1 = cursor.fetchall()
        for i in range(0,result[0]):
            tree.insert('', i, values=(result1[i]))

        lable2 = tk.Label(acs1, text='请输入还书信息：' , font=('微软雅黑', 20)).place(x=80, y=360)
        lable22=tk.Label(acs1, text='书名作者都要填写正确无误！' , font=('微软雅黑', 20)).place(x=80, y=400)
        global b_name
        tk.Label(acs1, text='书名：', font=('宋体', 12) ).place(x=80, y=480)
        b_name = tk.Entry(acs1, font=('宋体', 12) , width=10)
        b_name.place(x=130, y=480)

        global author
        tk.Label(acs1, text='作者：', font=('宋体', 12)).place(x=230, y=480)
        author = tk.Entry(acs1, font=('宋体', 12), width=10)
        author.place(x=280, y=480)

        tk.Button(acs1, text='确认还书', font=('宋体', 12), width=10, command=confirm_turnback).place(x=395, y=480)
    db.close()

def confirm_turnback():
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='acs',
        password='123',
        db='library',
        charset='utf8'
    )
    cursor = db.cursor()

    sql1 = 'UPDATE book SET amount=amount+1 WHERE name=%s AND author=%s'
    cursor.execute(sql1,(b_name.get(), author.get()))
    db.commit()

    time1=dt.datetime.now()#获取现在的时间
    sql2='SELECT date FROM borrow WHERE bookname=%s AND author=%s'
    cursor.execute(sql2,(b_name.get(),author.get()))
    result = cursor.fetchone()
    day=(time1-result[0]).days#得到时间差，检查图书是否超期
    print(day)
    if day>30:
        msg.showinfo(title='还书成功', message='还书成功，但您已经超期！请下次按时归还')
    else:
        msg.showinfo(title='还书成功', message='还书成功，且未超过30天')

    sql0 = 'DELETE FROM borrow WHERE bookname=%s AND author=%s'
    cursor.execute(sql0,(b_name.get(), author.get()))
    db.commit()
    db.close()
    acs1.destroy()

