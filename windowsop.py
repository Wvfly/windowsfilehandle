#_*_ coding: utf-8 _*_
#from winfilehandle import filehandle
import os

if __name__ == '__main__':
    conf='pathlist.txt'
    with open(conf, encoding='utf-8', errors='ignore') as cf:
        for i in cf.readlines():
            dir=i.strip()
            print(dir)
            try:
                os.makedirs(dir)
            except Exception as e:
                print(e)
            print(os.listdir(dir))

    a=input('enter to exit !')
