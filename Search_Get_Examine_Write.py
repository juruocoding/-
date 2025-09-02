import requests
import Write
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
import redef Examine(cnch,html,mode):
    soup = BeautifulSoup(html, "html.parser")
 
    div=soup.find("div", class_="view_con clearfix")#得到的是一个节点
    notes=str(div)
    cnch=str(cnch)
    if mode==2 or mode==3:
        pattern = r';[\u4e00-\u9fff\uFF1B]+。'
        lst=re.findall(pattern,notes)
        info=""
        for match in lst:
            info=info+match.replace(";","->")+"\n"
        messagebox.showinfo(cnch,info)
    if mode==3:
        pass
    Write.write(cnch,notes)

def Search_Get(cnch,text_utf8,mode):
    try:
        s_text=text_utf8.replace("\\","hw")
        url="https://wyw.hwxnet.com/view/"+s_text[2:17]+".html"
        r=requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        Examine(cnch,r.text,mode)
    except:
        print("请求失败")
def Function(cnch,text_utf8,mode):  
    Search_Get(cnch,text_utf8,mode)
    return
