from winfilehandle import filehandle
import os

if __name__ == '__main__':
    wfhandle=filehandle()
    conf='pathlist1.txt'

    # with open(conf, encoding='utf-8', errors='ignore') as cf:
    #     for i in cf.readlines():
    #         dir=i.strip()
    #         print(dir)
    #         try:
    #             os.makedirs(dir)
    #         except Exception as e:
    #             print(e)
    #         print(os.listdir(dir))

    with open(conf, encoding='utf-8', errors='ignore') as cf1:
        for i in cf1.readlines():
            dir=i.strip()
            print(dir)
            wfhandle.get_security_descriptor(dir)







