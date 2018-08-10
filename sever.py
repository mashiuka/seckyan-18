#sever側　ちょっとした実装済
import socket

# sever_addr = ('localhost',1234)
#
# sever = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sever.bind(sever_addr)
#
# max_size = 2048
# data, client = sever.recvfrom(max_size)

addres = ("localhost", 1234)
max_size = 1000
print('DANGREOUS')
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.bind(addres)
sever.listen(5)
client,addr = sever.accept()
# sever.connect(addres)
data = client.recv(max_size)
# client,client = sever.accept()
# sever.bind(addres)
# massage,addr = sever.recv(200)

massage = data
massage = '{0}'.format(massage).decode('UTF-8')

if len(massage) <= 0  & len(massage) < 2048:
        print("ok")
        client.sendall(b'OK')

else:
    client.sendall(b"NO. RETRUN YOUR HOME")
    print('ERROR' + massage)

client.close()
sever.close()
