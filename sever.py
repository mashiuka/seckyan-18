import socket


addres = ("localhost", 1234)
max_size = 1000
try:
  sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  sever.bind(addres)
  sever.listen(1)
  client,addr = sever.accept()
  data = client.recv(max_size)

  massage = data
  massage = data.decode('UTF-8')

  while True:
    if len(massage) >= 0:
        print("ok")
        client.sendall(b'OK')
        break
    else:
        client.sendall(b"NO. RETRUN YOUR HOME")
        print('ERROR \n' + massage)
        break

    client.close()
    sever.close()

except OSError:
    print('失敗')