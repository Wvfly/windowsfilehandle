# 数据本地归档整理

import os,re

path=r'E:/PycharmProjects/get_win_share/dist/目录权限'
new_path=r'E:/PycharmProjects/get_win_share/dist/目录权限_归档'


for file in os.listdir(path):
    full_path='%s/%s' % (path,file)
    mf=open('%s' % full_path,encoding='utf-8', errors='ignore')
    mw=open('%s/%s' % (new_path,file),'a',encoding='utf-8', errors='ignore')
    mr = mf.readlines()
    for i in range(2,len(mr)):
        newmsg=mr[i]
        msgtmp1=re.sub('\)','',re.sub('\(','',newmsg))
        nauth=msgtmp1.split(',')[-1].strip()

        if nauth=='1179817':
            auth='只读'
        elif nauth=='1245631' or nauth=='2032127':
            auth='读写'
        else:
            auth='特殊权限'


        newrecorde='%s\t%s\t%s\t%s' % (msgtmp1.split(',')[0],msgtmp1.split(',')[1],msgtmp1.split(',')[2],auth)
        mw.write(newrecorde + '\n')
    mw.close()
    mf.close()