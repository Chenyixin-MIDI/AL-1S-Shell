

if __name__=="__main__":
    pass;
import getpass#unlook函数所需模块
import time
import os
import datetime

import tkinter as tk
from tkinter import filedialog

import win32con
import win32api
import time




def worklog_Write(includes):#工作日志
    if includes not in("", " ", "\n"):#跳过空事件
        with open("worklog.txt","a")as f:
            f.write(includes)
current_time = datetime.datetime.now()
worklog_Write(current_time.strftime("%Y-%m-%d %H:%M:%S")+"\n")
def select_file():
    root = tk.Tk()
    root.withdraw()  
    global file_path
    file_path = filedialog.askopenfilename()  
    
    if file_path=="":
        print("Choose file--None")
    elif os.path.isfile(file_path):
        print("Choose file--"+file_path)
    else:
        print("WrongPath")
    worklog_Write("choose_file:"+file_path+" ")
    return file_path

def unlock(lock):
    count=0
    unlock=""
    lock=lock.split(" d")
    for i in lock:
        if count>=70:
            unlock=unlock+"\n"
            count=0
        if i=="":
            pass;
        else:
            i=int(i)
            i=i-67130
            unlock=unlock+str(chr(i))
            count=count+1
    worklog_Write("unlock:"+unlock)
    return unlock


def unlook():
    key = getpass.getpass("请输入：")
    worklog_Write("unlookInput:"+key)
    return key

root=False

with open("set/welcomeWords.ini")as f:
    welcomeWords=f.read()
    welcomeWords_list=welcomeWords.split(" ")
    welcomeWords=""
    for i in welcomeWords_list:
        if i =="%time":
            current_time = datetime.datetime.now()
            i = current_time.strftime("%Y-%m-%d %H:%M:%S")
        elif i=="%greet":
            current_time = time.localtime()
            if time.strftime("%H", current_time)>'0' and time.strftime("%H", current_time)<'12':
                i="早上好"
            elif time.strftime("%H", current_time)>='12' and time.strftime("%H", current_time)<"6":
                i="下午好"
            else:
                i="晚上好"
        welcomeWords=welcomeWords+i+" "


print(welcomeWords)
worklog_Write("welcomeWords:"+welcomeWords+"\n")
c_first=""
while c_first not in ["esc","ESC"]:
    c_first=input(">>>")
    worklog_Write(c_first+"\n")
    c=c_first.split(' ')
    lenC=len(c)

    if c[0]=="set" and lenC>1:
        if os.path.exists("set/"+c[1]+".ini"):
            if lenC>2:
                if lenC==3 and c[2] not in ("-f","-fp","-fP"):
                    with open("set/"+c[1]+".ini","w")as f:
                        f.write(c[2])
                
                elif lenC==3 and c[2]=="-f":
                    file=select_file()
                    with open(file)as f:
                        fileInclude=f.read()
                    with open("set/"+c[1]+".ini","w"):
                        f.write(fileInclude)
                        
                elif lenC==3 and c[2] in ("-fp","-fP"):
                    file=select_file()
                    with open("set/"+c[1]+".ini","w"):
                        f.write(file)
                    
                elif lenC==4 and c[2]=="-f":
                    if os.path.exists(c[3]):
                        with open(c[3])as f:
                            fileInclude=f.read()
                        with open("set/"+c[1]+".ini")as f:
                            f.write(fileInclude)
                    else:
                        print(">>>不存在该文件——"+c[3])
                
                elif c[2] not in("-f","-fp","-fP"):
                    print(">>>参数"+c[2]+"有误")
                elif lenC>4:
                    print(">>>参数长度不正确")
                
            else:
                fileInclude=input(":")
                with open("set/"+c[1]+".ini","w")as f:
                    f.write(fileInclude)
        
        else:
            print(">>>没有"+c[1]+"这个设置")





    elif c[0]=="run" and lenC>1:
        if os.path.exists(c[1]) and lenC==3:
            if c[2] in ("-e","-E","-exe","-EXE"):#当做exe文件运行
                os.system(c[1])
            elif c[2] in ("-p","-P"):#视为python文件运行
                os.system("python "+c[1])

        elif c[1] in ("-f","-F") and lenC==2:#当做exe文件运行
            file=select_file()
            os.system(file)
        elif c[1] in ("-f","-F") and lenC==3:
            if c[2] in ("-e","-E","-exe","-EXE"):#当做exe文件运行
                file=select_file()
                os.system(file)
            elif c[2] in ("-p","-P"):#视为python文件运行
                file=select_file()
                os.system("python "+file)


        elif not os.path.exists(c[1]) and c[1] not in ("-f","-F"):
            print("错误：参数-"+c[1]+"有误")
        

    elif c[lenC-1] in ("-w","-W","-windows"):#windows命令函数
        if lenC>2:
            
            order=""
            
            for i in c[0:lenC-3]:
                order=order+i+" "
        else:
            order=c[0]


        os.system(order)


    elif c_first in ("time","Time"):
    
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(formatted_time)


    elif c[0]=="root":
        
        rootPassword_Input=unlook()
        rootPassword=""


    #对Root密码进行解密：
        with open("set/key.ini")as f:
            rootPassword_lock=f.read()
        
        rootPassword_lock=rootPassword_lock.split(" d")

        for i in rootPassword_lock:
            if i =="":
                pass;
            else:

                i=int(i)
                i=i-67130
                rootPassword=rootPassword+str(chr(i))


        if rootPassword_Input==rootPassword:
            print("Root权限已开启")
            root=True
        else:
            print("密码不正确")

    elif c[0] in ["pa","Pa","PA"]:
        if root:
            if lenC==2 and c[1] in ["-all","-A","-All","-a"]:
                with open("set/lock.ini")as f:
                    lock=f.read()
                print(unlock(lock))
        else:
            print("没有root权限")







