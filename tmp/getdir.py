import os

def get_directories_by_level(directory, level=0):
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
            directories.extend(get_directories_by_level(item_path, level + 1))
    return directories

# 要获取目录列表的目录路径
directory_path = 'E:\\运维工作2023'

# 获取每一层目录的列表
directories = get_directories_by_level(directory_path)
#print(directories)
# 打印结果
print("Directories by level:")
for level, directory in directories:
    #print(f"Level {level}: {directory}")
    print(directory)
