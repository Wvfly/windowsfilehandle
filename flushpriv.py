from winfilehandle import filehandle
import json,os,elevate

elevate.elevate(graphical=False)    #获取管理员权限
wfhandle=filehandle()
conf = 'pathtree.txt'

# 1，通过读取conf记录的目录清单，在目标机器上挨个创建目录
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

    #TODO:开启目录共享

# 2，通过加载权限清单文件，把权限明细刷到新目录上
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
            wfhandle.set_file_permissions(path,user,permission,index1,index2)

# 3，根据导出的用户清单“系统用户清单.json”进行系统用户的批量创建，默认密码123456
def create_user():
    with open(r'系统用户清单.json',encoding='utf-8', errors='ignore') as uf:
        userlist=json.loads(uf.read())
        for username,fullname in userlist.items():
            print(username,fullname)
            wfhandle.create_user(username,'123456',fullname)

# 4，根据清单文件“系统用户组清单.json”，把原系统的用户组复刻到新系统
def create_group():
    groupfile = open('系统用户组清单.json', encoding='utf-8', errors='ignore')
    glist = groupfile.read()
    gdict = json.loads(glist)
    for gpname, gpinfo in gdict.items():
        groupname = gpname
        userlist = gpinfo['userlist']
        comments = gpinfo['comments']

        wfhandle.create_group(groupname, comments)
        for user in userlist:
            wfhandle.add_user_to_group(user, groupname)
    groupfile.close()

# 5，开启目前共享
def share_activate():
    #TODO：开启目录共享
    pass


if __name__ == '__main__':
    create_dir()
    create_user()
    create_group()
    share_activate()
    flush()
    # wfhandle.delete_user('shareuser')
    enddo = input('Enter any key to exit :')