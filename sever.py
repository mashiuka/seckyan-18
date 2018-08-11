import socket

addres = ("localhost", 1234)
max_size = 1000

try:
  sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  sever.bind(addres)
  sever.listen(1)
  client,addr = sever.accept()
  data = client.recv(max_size)
  client.sendall(b'you said >>   ')
  client.sendall(data)
  massage = data
  massage = data.decode('UTF-8')
 
  if len(massage) >= 0:
        print("ok")
        client.sendall(b'\nOK')

  else:
        client.sendall(b"NO. RETRUN YOUR HOME")
        print('ERROR \n' + massage)
  
  client.close()
  sever.close()

except OSError:
    print('OSError')