def quantstrigfile(file):
    data = open(file, encoding = "utf-8")
    j = 0
    for i in data:
        j = j + 1
    data.close
    return j
        

def readfile(file):
    data = open(file, encoding = "utf-8")
    print(data.read(), end="")
    print()
    data.close

def findinfile(lastname,file):
    data = open(file, encoding = "utf-8")
    j = quantstrigfile(file)
    k = 0
    for i in range(j):
        strfile = data.readline() 
        # str1 = strfile[strfile.find(' ')+1:]
        # str2 =str1[0:str1.find(' ')+1]
        if lastname in strfile[strfile.find(' ')+1:][0:strfile[strfile.find(' ')+1:].find(' ')+1]:
            print(strfile, end = "")
            k = k + 1
    print(f"Найдено совпадений {k}")
    data.close

def addcontactinfile(addinfo,file):
    data = open(file, "a", encoding = "utf-8")
    data.write(str(quantstrigfile(file)+1) + ". " + addinfo + "\n") 
    print(f"добавлена информация {addinfo}")
    data.close

def delstrinfile(numberstr,file):
    data = open(file,"r",encoding = "utf-8")
    listfile = data.readlines()
    data.close
    data = open(file,"w",encoding = "utf-8")
    for i in listfile:
        if i[:i.find(' ')] != str(numberstr)+".": #and int(numberstr) < quantstrigfile(file)
           data.write(i)
    data.close

def checknumerentry(file):
    data = open(file, encoding = "utf-8")
    listfile1 = data.readlines()
    data.close
    data = open(file,"w",encoding = "utf-8")
    j = 0
    for i in listfile1:
        j = j + 1
        data.write(str(j)+"."+i[i.find(' '):])
    data.close

def changefile(fierstname,lastname,threename,numbertel,numberstr, file):
    data = open(file,"r",encoding = "utf-8")
    listfile = data.readlines()
    data.close
    data = open(file,"w",encoding = "utf-8")
    print()
    for i in listfile:
        if i[:i.find(' ')] == str(numberstr)+".":
            print(f"заменена запись {i}")
            i = "0. "+lastname+" "+fierstname+" "+threename+" "+numbertel+"\n"
        data.write(i)
    data.close