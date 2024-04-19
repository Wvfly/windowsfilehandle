import time,os

timestamp = 1631109555.1492825
print(type(timestamp))
time_tuple = time.localtime(timestamp)
date_str = time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)
print(date_str)


path='c:/tmuninst.ini'
print(os.stat(path))
