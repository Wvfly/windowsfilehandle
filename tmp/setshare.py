import win32net
import win32netcon

def share_folder(folder_path, share_name):
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





# Example usage:
folder_path = r'D:\sss1'
share_name = 'sss1'
share_folder(folder_path, share_name)
