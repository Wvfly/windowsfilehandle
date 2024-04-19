# 调用win32接口获取目录下的所有文件及其创建时间和创建人，依赖pywin32

import os,time
import win32api
import win32con
import win32security

def getown(path):
    FILENAME = path
    # open(FILENAME, "w").close()
    try:
        # 打印当前windows用户
        # print("I am", win32api.GetUserNameEx (win32con.NameSamCompatible))

        sd = win32security.GetFileSecurity(FILENAME, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        name, domain, type = win32security.LookupAccountSid(None, owner_sid)

        ownmsg = "%s\\%s" % (domain, name)
    except Exception as e:
        ownmsg = e

    return ownmsg

'''
sharelist=[
    "E:\\政策与流程\\20-账务体系建设（2023年）\\1-实业分册",
    "E:\\report\\65_bk",
    "E:\\子公司报表(Ⅱ)\\LocalUser\\bixm",
    "E:\\report\\jtbbhb",
    "D:\\D_driver\\TCL实业",
    "D:\\D_driver\\中环半导体报表",
    "D:\\J_driver\\任职资格项目",
    "D:\\J_driver\\会计信息",
    "D:\\D_driver\\其他",
    "D:\\J_driver\\内部控制",
    "D:\\J_driver\\合并会计报表",
    "E:\\report\\合并组共享",
    "D:\\J_driver\\品牌",
    "E:\\report\\团队建设",
    "E:\\report\\子公司报表",
    "E:\\子公司报表(Ⅱ)",
    "D:\\D_driver\\总部职能信息共享",
    "E:\\战略投资部",
    "E:\\投资项目资料归档",
    "D:\\J_driver\\授信数据",
    "E:\\政策与流程",
    "E:\\本部管理",
    "D:\\D_driver\\盈利预测",
    "E:\\直管企业报表",
    "D:\\D_driver\\税务相关资料",
    "D:\\J_driver\\管理会计",
    "D:\\J_driver\\统计资料",
    "E:\\report\\合并组共享\\董秘办",
    "D:\\D_driver\\财务信息化资料",
    "D:\\J_driver\\财务管理",
    "D:\\J_driver\\财务管理资料",
    "D:\\D_driver\\资料",
    "E:\\report\\部门共享资料"
]
'''
sharelist=[r'E:\运维工作2024']

if __name__ == '__main__':

    for i in sharelist:

        sharename=i.split('\\')[-1]
        # print(sharename)
        wf=open(sharename + '.txt',"w",encoding='utf-8', errors='ignore')

        for root,dirs,paths in os.walk(i):
            for pathfile in paths:
                try:
                    files=os.path.join(root,pathfile)
                    print(files)
                    timetmp=os.stat(files).st_ctime
                    time_tuple = time.localtime(timetmp)
                    date_str = time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)
                    fileowner = getown(files)
                    wf.write('文件： %s --创建时间： %s --创建人： %s\n' % (files,date_str,fileowner))
                except Exception as e:
                    print(e)
        wf.close()


    #input('enten to exit')