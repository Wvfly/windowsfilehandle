from winfilehandle import filehandle
import json,os
wfhandle=filehandle()

# 通过读取conf中记录的目录清单，把目录的权限导出json格式（权限输出记录.json）
def download_priv():
    priv={}
    with open(conf, encoding='utf-8', errors='ignore') as cf1:
        for i in cf1.readlines():
            dir=i.strip()
            #print(dir)
            priv[dir]=wfhandle.get_security_descriptor(dir)
    #print(priv)
    pathpriv=json.dumps(priv,ensure_ascii=False,indent=4)
    with open(r'export\权限输出记录.json','w',encoding='utf-8', errors='ignore') as w:
        w.write(pathpriv)


if __name__ == '__main__':
    conf='pathlist1.txt'

    download_priv()







