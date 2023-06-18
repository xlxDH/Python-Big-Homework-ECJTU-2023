import tkinter as tk
import reader
import manager

def frame():
    global acs
    acs = tk.Tk()
    acs.geometry('800x600')
    acs.title('睡前消息图书管理系统')

    canvas=tk.Canvas(acs,height=1200,width=900)
    image_file=tk.PhotoImage(file='background.gif')
    image=canvas.create_image(-100,0,anchor='nw',image=image_file)
    canvas.place(x=0,y=0)


    lable0=tk.Label(acs,text='欢迎来到睡前消息',font=('微软雅黑',50),fg='GhostWhite',bg='MediumOrchid').pack()
    

    lable1=tk.Label(acs,text='请选择用户类型',font=('微软雅黑',20),fg='GhostWhite',bg='MediumOrchid').place(x=80,y=485)
    tk.Button(acs,text='读 者',font=('黑体',15),width=10,height=2,fg='GhostWhite',bg='MediumOrchid',command=exit_reader).place(x=350,y=420)
    tk.Button(acs,text='管理员',font=('黑体',15),width=10,height=2,fg='GhostWhite',bg='MediumOrchid',command=exit_manager).place(x=350,y=550)
    acs.mainloop()

def exit_reader():
    acs.update()
    acs.destroy()
    reader.frame()

def exit_manager():
    acs.update()
    acs.destroy()
    manager.frame()

if __name__ == '__main__':
    frame()