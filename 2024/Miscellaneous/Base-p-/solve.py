import base65536

with open('based.txt','r') as f:
    ct = f.readline().rstrip().replace(' ','')

with open('output','wb') as f2:
    f2.write(base65536.decode(ct))
