# import win32api
# import win32net
# import win32security
#
#
# def list_users():
#     try:
#         users, _, _ = win32net.NetUserEnum(None, 0)
#         for user in users:
#             print(f"User: {user['name']}")
#     except Exception as e:
#         print(f"Error listing users: {e}")
#
#
# def list_groups():
#     try:
#         groups, _, _ = win32net.NetLocalGroupEnum(None, 0)
#         for group in groups:
#             print(f"Group: {group['name']}")
#     except Exception as e:
#         print(f"Error listing groups: {e}")
#
#
# if __name__ == "__main__":
#     list_users()
#     list_groups()


import win32api
import win32net
import win32security


def get_user_info(username):
    try:
        # 获取用户详细信息，级别1004包含用户全名
        user_info = win32net.NetUserGetInfo(None, username, 2)
        full_name = user_info['full_name']
        # print(f"用户名: {username}")
        # print(f"全名: {full_name}")
        msg='%s\t%s' % (username,full_name)
        print(msg)
        with open('系统用户明细导出.txt',"a",encoding='utf-8', errors='ignore') as userfile:
            userfile.write(msg + '\n')
    except Exception as e:
        print(f"获取用户{username}信息时出错: {e}")


def get_group_info(groupname):
    try:
        # 获取组的基本信息
        group_info = win32net.NetLocalGroupGetInfo(None, groupname, 1)
        group_comment=group_info['comment']
        # print(f"组名: {groupname}")
        # print(f"描述: {group_info['comment']}")

        # print(msg)

        # 获取组内的用户列表
        users, _, _ = win32net.NetLocalGroupGetMembers(None, groupname, 1)
        # print("组内用户:")
        userlist=''
        for user in users:
            userlist += user['name'] + ','
            # print(f"    {user['name']}")

        msg = '%s\t%s\t%s' % (groupname, group_comment,userlist)
        print(msg)
        with open('系统用户组明细导出.txt', "a", encoding='utf-8', errors='ignore') as groupfile:
            groupfile.write(msg + '\n')

    except Exception as e:
        print(f"获取组{groupname}信息时出错: {e}")


def list_users():
    try:
        users, _, _ = win32net.NetUserEnum(None, 0)
        for user in users:
            get_user_info(user['name'])
    except Exception as e:
        print(f"列出用户时出错: {e}")


def list_groups():
    try:
        groups, _, _ = win32net.NetLocalGroupEnum(None, 0)
        for group in groups:
            get_group_info(group['name'])
    except Exception as e:
        print(f"列出组时出错: {e}")


if __name__ == "__main__":
    # 列出所有用户及其信息
    list_users()

    # 列出所有组及其信息和成员
    list_groups()

    a=input('enter to exit : ')