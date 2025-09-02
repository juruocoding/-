def write(cnch,notes):
    #请在route的''内更改wenyan.html的路径
    route=r'D:/StudyPython/python_try/requests/wenyan/wenyan.html'
    with open(route, 'a', encoding='utf-8') as file:
        file.write("<b>"+cnch +"</b>"+"\n"+notes+"\n")
if __name__=="__main__":
    write("文言实词记录","努力进步\n")
