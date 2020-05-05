

from tkinter import  *
from  selenium  import webdriver
import time
def  batch_reset_password(login_user,login_password,um_account_file,need_reset_password):
    the_file = um_account_file.replace('\\','/')
    return the_file

def  single_reset_password(login_user,login_password,um_account,need_reset_password):
    str = "chenyaozhang重置成功"
    return str


def  initial_um_input():
    max_thread_input.config(state=DISABLED)
    max_thread_input.update()
    um_label = Label(reset_window, text="请输入UM账号 : ", anchor=E, font=('微软雅黑', 9), )
    um_input = Entry(reset_window, width=50, textvariable=get_um_input)
    um_label.grid(row=5, column=0)
    um_input.grid(row=5, column=1, columnspan=2)
    um_label.update()
    um_input.update()

def  initial_file_input():

    max_thread_input.config(state=NORMAL)
    max_thread_input.update()
    um_label = Label(reset_window, text="请输入文件名称 : ", anchor=E, font=('微软雅黑', 9), )
    um_input = Entry(reset_window, width=50, textvariable=get_um_input)
    um_label.grid(row=5, column=0)
    um_input.grid(row=5, column=1, columnspan=2)
    um_label.update()
    um_input.update()

def  reset_password():
    execute_info_text.delete(0.0, END)
    btn1.config(state=DISABLED)
    reset_window.update()
    login_user = login_user_input.get()          #xx系统登录账号
    login_password = login_password_input.get()   #xx系统登录密码
    um_account = get_um_input.get()              #需要重置密码的UM账号 或 excel文件
    need_reset_password = new_password.get()     #重置后的UM密码
    try:
        max_thread = get_max_thread.get()
        get_max_thread.set(max_thread)
        if  max_thread > 10  or  max_thread < 1 :
            execute_info_text.insert(INSERT, "最大线程数大于10或小于1或输入非法字符，默认设置为5！" + '\n')
            get_max_thread.set(5)
            max_thread = get_max_thread.get()
    except:
        get_max_thread.set(5)
        max_thread = get_max_thread.get()
        execute_info_text.insert(INSERT, "最大线程数大于10或小于1或输入非法字符，默认设置为5！" + '\n')
    execute_info_text.insert(INSERT, "重置失败请检查XX系统能否登录，或重新尝试，谢谢！\n"
                                     "开始重置UM密码，请耐心等待...\n")
    execute_info_text.see(END)
    reset_window.update()
    if  '.xlsx' in um_account or '.XLSX' in um_account :
        result = batch_reset_password(login_user,login_password,um_account,need_reset_password)
    else:
        result = single_reset_password(login_user,login_password,um_account,need_reset_password)
    execute_info_text.insert(INSERT, result + um_account+" " + str(max_thread)+need_reset_password +'\n')
    btn1.config(state=NORMAL)






if __name__ =='__main__':
    reset_window = Tk()
    reset_window.title("重置UM密码")
    reset_window.geometry('600x550')
    reset_window.resizable(0,0)
    #设置说明文字
    explain_text = '说明：\n1、登录账号、密码指XX系统登录账号及密码。\n' \
                   '2、批量重置时如果excel文件和exe文件不在同一目录下，需要带上文件所在路径。\n' \
                   '3、选中批量重置时，最大线程数才会生效。线程数请输入1到10的正整数。'
    explain_label = Label(reset_window, text=explain_text, anchor=E, font=('微软雅黑', 9), justify=LEFT,foreground='red')
    explain_label.grid(row=0, column=0, columnspan=2)
    #用于获取XX系统登录信息的控件
    login_user_input = StringVar(value='umtest')
    login_password_input = StringVar(value='2333')
    user_label = Label(reset_window, text="请输入系统登录账号: ", anchor=E, font=('微软雅黑', 9,),)
    password_input = Entry(reset_window,textvariable= login_user_input,width=50,)
    user_label.grid(row=1, column=0)
    password_input.grid(row=1, column=1,columnspan=2,)
    password_label = Label(reset_window, text="请输入系统登录密码: ", anchor=E, font=('微软雅黑', 9), )
    password_input = Entry(reset_window,textvariable= login_password_input,width=50,)
    password_label.grid(row=2, column=0)
    password_input.grid(row=2, column=1,columnspan=2,)
    var =StringVar()
    var.set('A')
    ra1 = Radiobutton(reset_window,text="单个重置",variable=var,value='A',command=initial_um_input)
    ra1.grid(row=3, column=0)
    ra2 = Radiobutton(reset_window, text="批量重置",variable=var, value='B', command=initial_file_input)
    ra2.grid(row=3, column=1)
    #设置最大线程数
    get_max_thread = IntVar()
    get_max_thread.set(5)
    max_thread_label = Label(reset_window, text="设置最大线程数 : ", anchor=E, font=('微软雅黑', 9), )
    # validate="focusout", validatecommand=_valid_input_content
    max_thread_input = Entry(reset_window, width=50, textvariable=get_max_thread, state=DISABLED)
    max_thread_label.grid(row=4, column=0)
    max_thread_input.grid(row=4, column=1, columnspan=2)
    #用于获取需要重置的um账号及密码信息 的控件
    get_um_input = StringVar()
    default_um_label = Label(reset_window, text="请输入UM账号 : ", anchor=E, font=('微软雅黑', 9), )
    default_um_input = Entry(reset_window, width=50, textvariable=get_um_input)
    default_um_label.grid(row=5, column=0)
    default_um_input.grid(row=5, column=1, columnspan=2)
    new_password = StringVar()
    new_password.set("ummima@001")
    password_label = Label(reset_window, text="请输入重置后的UM密码: ", anchor=E, font=('微软雅黑', 9), )
    password_input = Entry(reset_window,textvariable=new_password,width=50,)
    password_label.grid(row=6, column=0)
    password_input.grid(row=6, column=1,columnspan=2,)
    #command = reset_password
    btn1 = Button(reset_window, text="重置密码",command = reset_password )
    btn1.grid(row=7, column=1,)

    #设置实时输出内容的控件
    text_value = StringVar()
    execute_info_text = Text(reset_window,width=50,padx=5,pady=5,height=15,font=('微软雅黑', 9))
    execute_info_text.grid(row=8,column=1,columnspan=2,sticky=S + W + E + N)
    #设置滚动条
    s1 = Scrollbar(orient="vertical",command=execute_info_text.yview)
    execute_info_text.config(yscrollcommand = s1.set)
    s1.grid(row=8, column=3, sticky=S + W + E + N)
    reset_window.mainloop()



