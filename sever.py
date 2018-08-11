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


  if massage == "NO NAME":
        print("no name")   
        client.sendall(b"\nRETRUN")
 
  elif len(massage) >= 0:
        print("ok")
        client.sendall(b'\nOK')

  else:
      print('ERROR')
  client.close()
  sever.close()

except OSError:
    print('OSError')
