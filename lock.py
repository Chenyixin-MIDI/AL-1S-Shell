password=input("")
P_list=list(password)
password_str=""
for i in P_list:
    _ord=ord(i)
    password_str=password_str+str(_ord+67130)+" d"
path=input("path")
with open(path,"w")as f:
    f.write(password_str)



