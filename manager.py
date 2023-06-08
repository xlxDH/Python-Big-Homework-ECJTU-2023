import tkinter as tk
import tkinter.messagebox as msg
import init
import pymysql
import idus

def frame():
    global acs
    acs = tk.Tk()
    acs.geometry('800x600')
    acs.title('睡前消息图书管理系统')

    canvas=tk.Canvas(acs,height=1200,width=900)#中
    image_file=tk.PhotoImage(file='background.gif')
    image=canvas.create_image(-100,0,anchor='nw',image=image_file)
    canvas.place(x=0,y=0)


    lable0=tk.Label(acs,text='管理员登录',font=('微软雅黑',50),fg='GhostWhite',bg='MediumOrchid').pack()
    

    lable1=tk.Label(acs,text='请选择',font=('微软雅黑',20),fg='GhostWhite',bg='MediumOrchid').place(x=200,y=450)
    tk.Button(acs,text='登 录',font=('黑体',15),width=10,height=2,fg='GhostWhite',bg='MediumOrchid',command=login).place(x=550,y=300)
    tk.Button(acs,text='注 册',font=('黑体',15),width=10,height=2,fg='GhostWhite',bg='MediumOrchid',command=register).place(x=550,y=400)
    tk.Button(acs,text='退 出',font=('黑体',15),width=10,height=2,fg='GhostWhite',bg='MediumOrchid',command=exit_manager).place(x=550,y=500)
    acs.mainloop()

def login():
    global root1
    root1=tk.Tk()
    root1.wm_attributes('-topmost', 1)
    root1.title('管理员登录')
    root1.geometry('500x300')

    lable1 = tk.Label(root1, text='账号：', font=25).place(x=100,y=50)
    lable2 = tk.Label(root1, text='密码：', font=25).place(x=100, y=100)

    global entry_name, entry_key
    name=tk.StringVar()
    key = tk.StringVar()

    entry_name = tk.Entry(root1, textvariable=name, font=25)
    entry_name.place(x=180, y=50)
    entry_key = tk.Entry(root1, textvariable=key, font=25,show='*')
    entry_key.place(x=180,y=100)
    button1 = tk.Button(root1, text='确定', height=2, width=10, command=lambda: idus.id_check('1'))
    button1.place(x=210, y=180)

def register():#注册小窗口
    global root2
    root2 = tk.Tk()
    root2.wm_attributes('-topmost', 1)
    root2.title('管理员注册')
    root2.geometry('500x300')

    lable1 = tk.Label(root2, text='账号：', font=25).place(x=100, y=50)
    lable2 = tk.Label(root2, text='密码：', font=25).place(x=100, y=100)
    lable2 = tk.Label(root2, text='确认密码：', font=25).place(x=80, y=150)

    global entry_name, entry_key, entry_confirm
    name = tk.StringVar()
    key = tk.StringVar()
    confirm = tk.StringVar()
    entry_name = tk.Entry(root2, textvariable=name, font=25)
    entry_name.place(x=180, y=50)
    entry_key = tk.Entry(root2, textvariable=key, font=25, show='*')
    entry_key.place(x=180, y=100)
    entry_confirm = tk.Entry(root2, textvariable=confirm,font=25, show='*')
    entry_confirm.place(x=180, y=150)
    button1 = tk.Button(root2, text='确定', height=2, width=10, command=lambda: idus.id_write('1'))
    button1.place(x=210, y=200)

def exit_manager():
    acs.destroy()
    init.frame()