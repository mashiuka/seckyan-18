import socket

# sever_addr = ('localhost',1234)
# max_size = 2086
# client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# massage = input()
# client.sendto(massage,sever_addr)
# data, sever = client.recvfrom(max_size)
# print('At',sever,'said')
# client.close()

addres = ('localhost', 1234)
max_size = 320
masage  = input()
masage = '{0}'.format(masage).encode('utf-8')
print(masage)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addres)
client.sendall(masage)
data = client.recv(max_size)

print(data)

client.close()
