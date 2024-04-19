# 获取目录的权限

import win32security
# import ntsecuritycon as con

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
sharelist=[r'D:\sss1']

for FILENAME in sharelist:
    sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)
    dacl = sd.GetSecurityDescriptorDacl()
    ace_count = dacl.GetAceCount() #显示具有文件夹权限用户(组)数量
    print('目录权限：%s' % FILENAME)
    print('Ace count:', ace_count)
    pathname=FILENAME.split('\\')[-1]
    print(pathname)

    wf=open(pathname + '.txt',"w",encoding='utf-8', errors='ignore')
    wf.write('目录权限：%s\n' % FILENAME)
    wf.write('有权限的用户数: %s\n' % ace_count)
    for i in range(0, ace_count):
        try:
            rev, access, usersid = dacl.GetAce(i)
            #print(rev,access,usersid)
            user, group, type = win32security.LookupAccountSid('', usersid)
            msg='User: {}/{}'.format(group, user), rev, access, type
            print(msg)
            wf.write(str(msg) + '\n')
        except Exception as e:
            print(e)
    wf.close()


#a=input('enter to exit: ')