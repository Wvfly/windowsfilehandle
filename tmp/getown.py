import win32api
import win32con
import win32security,time

a=input('enter: ')
#FILENAME = input('file: ')
FILENAME = 'D:\\D_driver\\盈利预测\\2024年盈利预测\\202403\\创投科技侧2024年Q1经营预测@240226.xlsx'
#open(FILENAME, "w").close()

try:
    # 打印当前windows用户
    # print("I am", win32api.GetUserNameEx (win32con.NameSamCompatible))

    sd = win32security.GetFileSecurity (FILENAME, win32security.OWNER_SECURITY_INFORMATION)
    owner_sid = sd.GetSecurityDescriptorOwner ()
    name, domain, type = win32security.LookupAccountSid (None, owner_sid)

    print("File owned by %s\\%s" % (domain, name))
except Exception as e:
    print(e)

input('enter to exit')
