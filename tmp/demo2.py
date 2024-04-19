import win32api
import win32net
import win32security


def get_user_info(username):
    try:
        # 获取用户详细信息，级别1004包含用户全名
        user_info = win32net.NetUserGetInfo(None, username, 1004)
        full_name = user_info['full_name']
        print(f"用户名: {username}")
        print(f"全名: {full_name}")
    except Exception as e:
        print(f"获取用户{username}信息时出错: {e}")

def get_group_info(groupname):
    try:
        # 获取组的基本信息
        group_info = win32net.NetLocalGroupGetInfo(None, groupname, 0)
        print(f"组名: {groupname}")
        print(f"描述: {group_info['description']}")

        # 获取组内的用户列表
        users, _, _ = win32net.NetLocalGroupGetMembers(None, groupname, 1)
        print("组内用户:")
        for user in users:
            print(f"    {user['name']}")
    except Exception as e:
        print(f"获取组{groupname}信息时出错: {e}")


user_info = win32net.NetUserGetInfo(None, 'wwg', 3)
print(user_info)

group_info = win32net.NetLocalGroupGetInfo(None, 'Users', 1)
print(group_info)

users, _, _ = win32net.NetLocalGroupGetMembers(None, 'Administrators', 1)
userlist=''
for user in users:
    userlist += user['name'] + ','
print(userlist)


win32net.

