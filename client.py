import socket

addres = ('localhost', 1234)
max_size = 1000
masage  = input()
if len(masage) is 0:
    masage = "NO NAME"
masage = '{0}'.format(masage).encode('utf-8')

print(masage) #何を送るか
try:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(addres)
    client.sendall(masage)
    data = client.recv(max_size)
    data1 = data.decode('UTF-8') 
    print(data1)
    client.close()

except ConnectionRefusedError:
    print('失敗')
