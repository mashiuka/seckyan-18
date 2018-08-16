 #!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
from scapy.all import *

stment =  " COMMAND LINE EROOR { COMMAND LINE IS limited to 3 and COMMAND LINE is　Less than 2 } "
argc = len(sys.argv)
argv = sys.argv
print(argc)

class Send_processing():
    def __init__(self,ip,port): #引数　ネットワーク接続
        self.ip = ip
        self.port = port

    def tcp(self):#tcpの処理
        ip = IP(dst = self.ip)
        seq = 1000000
        for i in xrange(1,51):
            port = i
            sport = random.randint(50000,60000)
            tcp = TCP(sport = sport,dport = port, seq = seq , flags = 'S')
            recv = sr1(ip/tcp,verbose = False)

            if recv['TCP'].flags == "SA":
                print('{0}/TCP : open '.format(i))

            elif recv['TCP'].flags == "RA":
                print('{0}/TCP : close'.format(i))

def commandline(argc,argv): #cuiのコマンドライン実装機能 できればmanまで
    if argc >= 3:
        print('To start the ' + argv[1]) #3個だった場合タプルで(1,2)や(2,4)など
        return True

    elif argc <= 1 :
        print('Argument is missing - Few Argument')
        print(stment)
        return False

    elif argc > 4:
        print('Argument is missing - many Argument')
        print(stment)
        return False

def treatment_def(i,p):#Send_processingを使う
     treatment = Send_processing(i,p)
     treatment.tcp()

def main():#通信やフレームワークなどの設定
    commandline(argc,argv)
    treatment_def(argv[1],0)#"172.16.212.254"

if __name__ == "__main__":
    main()
