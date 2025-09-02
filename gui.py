import tkinter as tk
from tkinter import messagebox
import Search_Get_Examine_Write as sgew

def create_gui():
    # 创建主窗口
    window = tk.Tk()
    window.title("简单文言程序 搜索 记录一体")
    window.geometry("900x600")
    
    # 定义字体样式
    title_font = ("Arial", 16, "bold")  # 标题字体
    label_font = ("Arial", 12)          # 普通标签字体
    entry_font = ("Arial", 12)          # 输入框字体
    button_font = ("Arial", 12, "bold") # 按钮字体
    
    # 添加标题标签
    title_label = tk.Label(window, text="文言字词释义搜索程序", font=title_font)
    title_label.pack(pady=40)
    
    # 添加说明标签
    label = tk.Label(window, text="请输入要搜索的文言字词内容:(单个汉字)", font=label_font)
    label.pack(pady=10)
    
    # 添加输入框
    chcn_entry = tk.Entry(window, width=40, font=entry_font)
    chcn_entry.pack(pady=10)

    user_text=""
    text_utf8=""
    cnch=""
    
    def Init():
        global user_text
        global text_utf8
        global cnch
        global route
        user_text = chcn_entry.get()
#        route =route_entry.get()
        # 将文本编码为UTF-8字节串
        text_utf8=user_text.encode("utf-8")
        cnch=str(user_text)  #Chinese_character
        text_utf8=repr(text_utf8)
        # 传递处理后的字符串给搜索函数
        
    # 按钮点击事件处理
    def on_button1_click():
        Init()
        global user_text,cnch,text_utf8
        sgew.Function(cnch, text_utf8,1)
        if user_text:
            pass
        else:
            messagebox.showwarning("警告", "请输入一些内容")
    
    # 添加按钮1
    button1 = tk.Button(window, text="搜索文言释义(仅记录在文件中)", command=on_button1_click, font=button_font, 
                      width=35, height=2, bg="#4CAF50", fg="white")
    button1.pack(pady=15)


    def on_button2_click():
        Init()
        global user_text,cnch,text_utf8
        sgew.Function(cnch,text_utf8,2)
        if user_text:
            pass
        else:
            messagebox.showwarning("警告", "请输入一些内容")
    # 添加按钮2
    button2 = tk.Button(window, text="搜索文言释义(记录+显示)", command=on_button2_click, font=button_font, 
                      width=35, height=2, bg="#4CAF50", fg="white")
    button2.pack(pady=15)


    def on_button3_click():
        Init()
        global user_text,cnch,text_utf8
        sgew.Function(cnch, text_utf8,3)
        if user_text:
            pass
        else:
            messagebox.showwarning("警告", "请输入一些内容")
    # 添加按钮3
    button3 = tk.Button(window, text="搜索文言释义(仅显示)", command=on_button3_click, font=button_font, 
                      width=35, height=2, bg="#4CAF50", fg="white")
    button3.pack(pady=15)
    # 退出按钮
    quit_button = tk.Button(window, text="退出程序", command=window.quit, font=button_font,
                           width=15, height=2, bg="#f44336", fg="white")
    quit_button.pack(pady=10)
    
    # 运行主循环
    window.mainloop()

if __name__ == "__main__":
    create_gui()
