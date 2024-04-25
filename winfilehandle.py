import win32security,win32netcon,win32net,win32con,win32api,os,json

class filehandle():
    '''
    windows文件和用户权限操作工具集
    '''
    def __init__(self):
        pass

    # 创建空白acl
    def create_acl(self):
        acl = win32security.ACL()
        return acl

    # 获取当前访问控制列表
    def current_acl(self,FILENAME):
        # acl = win32security.ACL()
        sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)
        acl = sd.GetSecurityDescriptorDacl()
        return acl

    # 在当前控制列表的基础上上添加新的访问控制项
    def add_access_control_entry(self,acl, sid, permissions, index1=3,index2=1179817):
        #acl.AddAccessAllowedAce(ntsecuritycon.FILE_ALL_ACCESS, sid)
        if permissions == 0:
            # acl.AddAccessAllowedAceEx(win32security.ACL_REVISION, 11, -1610612736, sid)     #设置为允许的权限
            # acl.AddAccessAllowedAceEx(win32security.ACL_REVISION, 0, 1179817, sid)
            acl.AddAccessAllowedAceEx(win32security.ACL_REVISION, index1, index2, sid)
        elif permissions == 1:
            acl.AddAccessDeniedAceEx(win32security.ACL_REVISION, index1, index2, sid)       #设置为拒绝的权限
        else:
            raise AssertionError('permission参数 "%s" :权限参数错误或未指定，0允许,1拒绝' % permissions)

    def delete_acl(self,path,username):
        try:
            # 获取文件或目录的安全描述符
            sd = win32security.GetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION)
            # 获取安全描述符中的DACL
            dacl = sd.GetSecurityDescriptorDacl()
            # 遍历DACL中的ACE
            sid_index = []
            for i in range(dacl.GetAceCount()):
                rev, access, usersid = dacl.GetAce(i)
                # 检查ACE所适用的用户是否与指定用户匹配
                if win32security.LookupAccountSid(None, usersid)[0] == username:
                    sid_index.append(i)

            for j in range(len(sid_index)):
                dacl.DeleteAce(sid_index[j] - j)

            # 将修改后的DACL应用到文件或目录
            sd.SetSecurityDescriptorDacl(1, dacl, 0)
            win32security.SetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION, sd)

            print(f"Removed permissions for user: {username}")
        except Exception as e:
            print(f"Error: {e}")

    # 把acl应用到对应目录上
    def set_security_descriptor_dacl(self,path, acl):
        sd = win32security.GetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION)
        sd.SetSecurityDescriptorDacl(1, acl, 0)
        win32security.SetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION, sd)

    # 获取文件或目录的安全描述符
    def get_security_descriptor(self,path):
        sd = win32security.GetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION)
        dacl = sd.GetSecurityDescriptorDacl()
        ace_count = dacl.GetAceCount()  # 显示具有文件夹权限用户(组)数量
        # print('目录权限：%s' % path)
        # print('Ace count:', ace_count)
        # pathname = path.split('\\')[-1]
        # print(pathname)

        # wf = open(pathname + '.txt', "w", encoding='utf-8', errors='ignore')
        # wf.write('目录权限：%s\n' % path)
        # wf.write('有权限的用户数: %s\n' % ace_count)

        returnmsg=[]

        for i in range(0, ace_count):
            try:
                rev, access, usersid = dacl.GetAce(i)
                user, group, type = win32security.LookupAccountSid('', usersid)
                lrev=list(rev)  #把rev从元组转为数组
                lrev.append(access)
                lrev.append(user)
                returnmsg.append(lrev)
                # print(lrev)

                # msg='%s,%s,%s' %
                # print()

                # msg = 'User: {}/{}'.format(group, user), rev, access, type
                # print(msg)

                # wf.write(str(msg) + '\n')
            except Exception as e:
                print(e)

        #print(returnmsg)
        return (returnmsg)
        # wf.close()

    def share_folder(self,folder_path, share_name):
        '''
        开启目前共享
        :param folder_path: 目录
        :param share_name: 一般与目录同名即可
        :return:
        '''
        info = {
            'netname': share_name,
            'path': folder_path,
            'remark': '',
            'max_uses': -1,
            'current_uses': 0,
            'permissions': (win32netcon.ACCESS_READ | win32netcon.ACCESS_WRITE | win32netcon.ACCESS_CREATE),
            'passwd': ''
        }
        win32net.NetShareAdd(None, 2, info)

    def get_own(self,path):
        '''
        获取文件/目录的创建人
        :param path:
        :return:
        '''
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

    # 总方法，设置文件/目录权限
    def set_file_permissions(self, file_path, user, permission, index1, index2):
        '''
        参数案例参考，例如原目录权限为('User: BUILTIN/Administrators', (0, 11), 268435456, 4)，
        则：
        permission=0，（0允许，1拒绝）
        index1=11,
        index2=268435456

        :param file_path: 目录
        :param user: 用户名
        :param permission: 权限（0或1）
        :param index1: 权限范围1
        :param index2: 权限范围2
        :return:
        '''
        acl = self.current_acl(file_path)
        sid = win32security.LookupAccountName(None, user)[0]
        self.add_access_control_entry(acl, sid, permission, index1, index2)
        self.set_security_descriptor_dacl(file_path, acl)

    def get_current_user(self):
        '''
        获取当前用户
        :return:
        '''
        return win32api.GetUserNameEx(win32con.NameSamCompatible)

    def get_user_info(self,username):
        msg={}
        try:
            # 获取用户详细信息，级别1004包含用户全名
            user_info = win32net.NetUserGetInfo(None, username, 2)
            fullname = user_info['full_name']
            # print(f"用户名: {username}")
            # print(f"全名: {full_name}")
            msgtmp = '用户名：%s\t用户全名：%s' % (username, fullname)
            msg[username]=fullname
            # with open('系统用户明细导出.txt', "a", encoding='utf-8', errors='ignore') as userfile:
            #     userfile.write(msgtmp + '\n')
        except Exception as e:
            msg=f"获取用户{username}信息时出错: {e}"
            print(msg)
        return msg

    def get_group_info(self,groupname):
        try:
            # 获取组的基本信息
            group_info = win32net.NetLocalGroupGetInfo(None, groupname, 1)
            group_comment = group_info['comment']
            # print(f"组名: {groupname}")
            # print(f"描述: {group_info['comment']}")

            # print(msg)

            # 获取组内的用户列表
            users, _, _ = win32net.NetLocalGroupGetMembers(None, groupname, 1)
            # print("组内用户:")
            userlist = ''
            for user in users:
                userlist += user['name'] + ','
                # print(f"    {user['name']}")

            msg = '组名：%s\t组描述信息：%s\t组成员：%s' % (groupname, group_comment, userlist)
            print(msg)
            with open('系统用户组明细导出.txt', "a", encoding='utf-8', errors='ignore') as groupfile:
                groupfile.write(msg + '\n')

        except Exception as e:
            print(f"获取组{groupname}信息时出错: {e}")

    def list_users(self):
        '''
        获取windows用户清单
        :return:返回用户和用户全名的json结构
        '''
        msg={}
        try:
            users, _, _ = win32net.NetUserEnum(None, 0)
            for user in users:
                userinfo=self.get_user_info(user['name'])
                msg.update(userinfo)
            msg=json.dumps(msg,ensure_ascii=False,indent=4)
        except Exception as e:
            msg=f"列出用户时出错: {e}"
        return msg


    def list_groups(self):
        '''
        获取windows用户组明细
        :return:
        '''
        try:
            groups, _, _ = win32net.NetLocalGroupEnum(None, 0)
            for group in groups:
                self.get_group_info(group['name'])
        except Exception as e:
            print(f"列出组时出错: {e}")

    def create_user(self,username, password, fullname, comment=None):
        '''
        1，特别注意：使用本方法创建用户需要以管理员身份运行
        2，可以在代码中调用 elevate.elevate(graphical=False) 获得管理员权限
        :param username:
        :param password:
        :return:
        '''

        data = {
            'name': username,
            'password': password,
            'password_age': 0,
            'full_name': fullname,
            'comment': comment,
            'acct_expires': 4294967295,
            'priv': 1,
            'flags': 66113
        }
        # 65513（用户不能修改密码，密码永不过期）
        # 65515（用户不能修改密码，密码永不过期，账号已禁用）

        # 使用 win32net.NetUserAdd() 创建用户
        win32net.NetUserAdd(None, 2, data)

    def delete_user(self,username):
        '''
        1，特别注意，使用本方法删除用户需要获得管理员权限
        2，可以在代码中调用 elevate.elevate(graphical=False) 获得管理员权限
        :param username:
        :return:
        '''
        try:
            # 使用 win32net.NetUserDel() 删除用户
            win32net.NetUserDel(None, username)
            print(f"User {username} deleted successfully.")
        except Exception as e:
            print(f"Error deleting user: {e}")

    # 要创建的用户名和密码
    # new_username = "newuser"
    # new_password = "newpassword"

    def get_directories_by_level(self,directory, level=0):
        '''
        获取指定目录的目录数结构
        :param directory:
        :param level:
        :return:
        '''
        # 创建一个空列表，用于存储当前层的所有目录
        directories = []
        # 遍历当前目录中的所有项
        for item in os.listdir(directory):
            # 拼接项的完整路径
            item_path = os.path.join(directory, item)
            # 检查项是否是一个目录
            if os.path.isdir(item_path):
                # 如果是目录，则将其添加到列表中
                directories.append((level, item_path))
                # 递归调用以获取子目录
                directories.extend(self.get_directories_by_level(item_path, level + 1))
        return directories



