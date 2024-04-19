
import win32security
import win32api
import win32con

def get_directory_security(folder_path):
    # 获取文件夹的安全描述符
    sd = win32security.GetFileSecurity(folder_path, win32security.DACL_SECURITY_INFORMATION)
    return sd

def extract_permissions(sd):
    # 从安全描述符中提取访问控制列表（ACL）
    dacl = sd.GetSecurityDescriptorDacl()

    # 遍历ACL并提取权限信息
    permissions = []
    for ace_no in range(dacl.GetAceCount()):
        ace = dacl.GetAce(ace_no)
        trustee_sid = ace[1]
        print(ace)
        trustee_name = win32security.ConvertSidToStringSid(ace[2])
        permissions.append((trustee_name, ace[2]))

    print(permissions)
    return permissions

def export_permissions(permissions, output_file):
    # 将权限信息写入文件
    with open(output_file, 'w') as f:
        for trustee_sid, access_rights in permissions:
            trustee_name = win32security.LookupAccountSid(None, win32security.ConvertStringSidToSid(trustee_sid))[0]
            f.write(f"Trustee: {trustee_name}\n")
            f.write("Access Rights:\n")
            for access_right in access_rights:
                f.write(f"  {access_right}\n")
            f.write("\n")

if __name__ == "__main__":
    folder_path = r'D:\service'
    output_file = 'permissions.txt'

    sd = get_directory_security(folder_path)
    print(sd)
    permissions = extract_permissions(sd)
    export_permissions(permissions, output_file)
