from winfilehandle import filehandle
import json
wfhandle=filehandle()
mainpathlist='pathlist.txt'
pathtreefile='pathtree.txt'

# 通过读取conf中记录的目录清单，把目录的权限导出json格式（权限输出记录.json）
def download_priv():
    priv={}
    with open(pathtreefile, encoding='utf-8', errors='ignore') as cf1:
        for i in cf1.readlines():
            dir=i.strip()
            #print(dir)
            priv[dir]=wfhandle.get_security_descriptor(dir)
    #print(priv)
    pathpriv=json.dumps(priv,ensure_ascii=False,indent=4)
    with open(r'export\权限输出记录.json','w',encoding='utf-8', errors='ignore') as w:
        w.write(pathpriv)


if __name__ == '__main__':
# 1，把共享目录的目录数据结构导出到“pathree.txt”
# 2，把pathtree.txt记录的目录树权限导出到“权限输出记录.txt”
    mf=open(mainpathlist,encoding='utf-8', errors='ignore')
    pathtmp=mf.readlines()
    # 把主目录的目录树结构下载到pathtree.txt
    for i in range(len(pathtmp)):
        mainpath=pathtmp[i].strip()
        print(mainpath)
        #mainpath=r'E:\运维工作2021'
        pathtree=wfhandle.get_directories_by_level(mainpath)

        pf=open(pathtreefile,'w',encoding='utf-8', errors='ignore')
        for j in range(len(pathtree)):
            inerpath=pathtree[j][1]
            pf.write(inerpath + '\n')
        pf.close()

        # 把每层目录的权限下载到‘权限输出记录.txt’
        download_priv()

    mf.close()

# 3，把系统用户导出到“系统用户清单.json”
    userinfo=wfhandle.list_users()
    print(userinfo)
    uf=open('系统用户清单.json','w',encoding='utf-8', errors='ignore')
    uf.write(userinfo)
    uf.close()






