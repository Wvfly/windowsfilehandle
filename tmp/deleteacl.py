import win32security


def remove_user_permission(file_path, user_name):
    # 获取文件或目录的安全描述符
    sd = win32security.GetFileSecurity(file_path, win32security.DACL_SECURITY_INFORMATION)

    # 获取安全描述符中的DACL
    dacl = sd.GetSecurityDescriptorDacl()
    # dacl.DeleteAce(8)
    # dacl.DeleteAce(8)

    # 遍历DACL中的ACE
    #print(dacl.GetAce)
    sid_index=[]
    for i in range(dacl.GetAceCount()):
        rev, access, usersid = dacl.GetAce(i)
        # 检查ACE所适用的用户是否与指定用户匹配
        if win32security.LookupAccountSid(None, usersid)[0] == user_name:
            # 如果匹配，则从DACL中移除该ACE
            #dacl.DeleteAce(i)
            sid_index.append(i)

    for j in range(len(sid_index)):
        dacl.DeleteAce(sid_index[j] - j)


    # 将修改后的DACL应用到文件或目录
    sd.SetSecurityDescriptorDacl(1, dacl, 0)
    win32security.SetFileSecurity(file_path, win32security.DACL_SECURITY_INFORMATION, sd)




# Example usage:
file_path = r'D:\sss1'
user_name = 'wwg'
remove_user_permission(file_path, user_name)
