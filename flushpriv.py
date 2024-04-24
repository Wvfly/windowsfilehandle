from winfilehandle import filehandle
import json,os

handle=filehandle()

# 通过读取conf记录的目录清单，在目标机器上挨个创建目录
def create_dir():
    with open(conf, encoding='utf-8', errors='ignore') as cf:
        for i in cf.readlines():
            dir=i.strip()
            print(dir)
            try:
                os.makedirs(dir)
            except Exception as e:
                print(e)
            print(os.listdir(dir))

# 通过加载权限清单文件，把权限明细刷到新目录上
def flush():
    privfile=r'export\权限输出记录.json'
    with open(privfile,encoding='utf-8', errors='ignore') as f:
        msg=f.read()
    priv_dict=json.loads(msg)

    for k,v in priv_dict.items():
        privlist=priv_dict[k]
        for i in range(len(privlist)):
            path=k
            permission=privlist[i][0]
            index1=privlist[i][1]
            index2=privlist[i][2]
            user=privlist[i][3]
            print(path,permission,index1,index2)
            handle.set_file_permissions(path,user,permission,index1,index2)


if __name__ == '__main__':
    conf = 'pathlist1.txt'
    flush()