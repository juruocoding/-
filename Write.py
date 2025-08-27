
def write(cnch,notes):
#    需要修改open后第一对双引号内的路径
    with open("D:\\StudyPython\\python_try\\requests\\wenyan\\wenyan.html", 'a', encoding='utf-8') as file:
        file.write("<b>" + cnch + "</b>" +"\n" + notes + "\n")

if __name__=="__main__":
    write("文言实词记录","努力进步")