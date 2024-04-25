from winfilehandle import filehandle

if __name__ == '__main__':
    handle=filehandle()
    file_path = r"D:\sss1"
    user = "test111"
    password = '123456'
    # handle.share_folder(file_path,'sss1')
    handle.create_user(user,password,'自动化测试用户3')
    #handle.set_file_permissions(file_path, user, 0, 3, 1179817)
    #handle.set_file_permissions(file_path, user, 0, 3, 1245631)

    # # 需要删除这两个用户组，否则出现权限异常
    # handle.delete_acl(file_path, 'Users')
    # handle.delete_acl(file_path, 'Authenticated Users')


    #handle.delete_acl(file_path,user)
    ##handle.get_security_descriptor(file_path)
    #print(win32net.US)
    #print(handle.get_own(file_path))

    #handle.create_user('qwert','123456','ceshi123133444')
    #handle.delete_user('qwert')
    # handle.list_users()
    # handle.list_groups()



    directory_path = 'E:\\运维工作2023'
    # 获取每一层目录的列表
    directories = handle.get_directories_by_level(directory_path)
    print(directories)
    # 打印结果
    print("Directories by level:")
    for level, directory in directories:
        #print(f"Level {level}: {directory}")
        print(directory)


    print(handle.get_current_user())