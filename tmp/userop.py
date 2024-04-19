import win32net
import win32netcon


userinfo={
    'name': 'wwg',
    'password': None,
    'password_age': 3016811,
    'priv': 1,
    'home_dir': '',
    'comment': '',
    'flags': 66113,
    'script_path': '',
    'auth_flags': 0,
    'full_name': '测试',
    'usr_comment': '',
    'parms': '',
    'workstations': '',
    'last_logon': 0,
    'last_logoff': 0,
    'acct_expires': 4294967295,
    'max_storage': 4294967295,
    'units_per_week': 168,
    'logon_hours': b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',
    'bad_pw_count': 0,
    'num_logons': 0,
    'logon_server': '\\\\*',
    'country_code': 0,
    'code_page': 0
}


def create_user(username, password):
    '''
    创建用户
    :param username:
    :param password:
    :return:
    '''

    data={
        'name':username,
        'password':password,
        'password_age':0,
        #'usr_comment': '测试11111111',
        'priv':1,
        'flags':66113
    }
    # 使用 win32net.NetUserAdd() 创建用户
    win32net.NetUserAdd(None, 1, data)


# 要创建的用户名和密码
new_username = "qwert"
new_password = "123456"

# 创建用户（在本地计算机上）
create_user(new_username, new_password)
