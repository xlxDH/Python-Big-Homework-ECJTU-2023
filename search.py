import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
import pymysql

def frame():
    global window
    window = tk.Tk()
    window.title('图书查询')
    window.geometry('1200x700')

    tk.Label(window,text='图书类目：',font=('宋体',12)).place(x=220,y=30)

    global list
    comvalue=tk.StringVar()
    list=ttk.Combobox(window,textvariable=comvalue,height=10,width=10)
    list.place(x=300,y=30)
    list['values']=('全部','人文','艺术','计算机','科技','杂志')
    list.current(0)

    global b_name
    tk.Label(window, text='书名：', font=('宋体', 12)).place(x=450, y=30)
    b_name=tk.Entry(window,font=('宋体', 12),width=15)
    b_name.place(x=500,y=30)

    global author
    tk.Label(window, text='作者：', font=('宋体', 12)).place(x=650, y=30)
    author = tk.Entry(window, font=('宋体', 12), width=15)
    author.place(x=700, y=30)

    tk.Button(window,text='搜索',font=('宋体', 12), width=10,command=search).place(x=900,y=25)
    global tree#建立树形图
    yscrollbar = ttk.Scrollbar(window, orient='vertical')#右边的滑动按钮
    tree = ttk.Treeview(window, columns=('1', '2', '3', '4', '5'), show="headings",yscrollcommand=yscrollbar.set)
    tree.column('1', width=150, anchor='center')
    tree.column('2', width=150, anchor='center')
    tree.column('3', width=150, anchor='center')
    tree.column('4', width=150, anchor='center')
    tree.column('5', width=150, anchor='center')
    tree.heading('1', text='类目')
    tree.heading('2', text='书名')
    tree.heading('3', text='作者')
    tree.heading('4', text='价格')
    tree.heading('5', text='库存')
    tree.place(x=200, y=150)
    yscrollbar.place(x=955,y=150)
    window.mainloop()

def search():
#我用了最原始的方法来动态查询
    if list.get()=='全部'and b_name.get()=='' and author.get()=='' :
        sql="SELECT * FROM book "
    elif list.get()=='全部'and b_name.get()=='' and author.get()!='' :
        sql="SELECT * FROM book WHERE author='%s'"%(author.get())
    elif list.get()=='全部'and b_name.get()!='' and author.get()=='' :
        sql = "SELECT * FROM book WHERE name='%s'" % (b_name.get())
    elif list.get() != '全部'  and b_name.get() =='' and author.get() == '' :
        sql = "SELECT * FROM book WHERE type='%s'" % (list.get())
    elif list.get()=='全部'and b_name.get() !='' and author.get()!= '' :
        sql = "SELECT * FROM book WHERE name='%s' AND author='%s'" % (b_name.get(),author.get())
    elif list.get() != '全部' and b_name.get() !='' and author.get() == '' :
        sql = "SELECT * FROM book WHERE type='%s' AND name='%s'" % (list.get(),b_name.get())
    elif list.get() != '全部' and b_name.get() =='' and author.get() != '' :
        sql = "SELECT * FROM book WHERE type='%s' AND author ='%s'" % (list.get(), author.get())
    else :
        sql = "SELECT * FROM book WHERE type='%s' AND name='%s' AND author ='%s'" % (list.get(),b_name.get(), author.get())

    db = pymysql.connect("localhost", "root", "asd1997727xu", "library")
    cursor = db.cursor()
    cursor.execute(sql)
    results=cursor.fetchall()
    if results:
        l= len(results)
        for i in range(0,l):#查询到的结果依次插入到表格中
            tree.insert('',i,values=(results[i]))
    else :
        tree.insert('', 0,values=('查询不到结果','查询不到结果','查询不到结果','查询不到结果','查询不到结果'))

    db.close()
