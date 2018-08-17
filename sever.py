 #!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import random
import sys
from scapy.all import *

stment =  " COMMAND LINE EROOR { COMMAND LINE IS limited to 3 and COMMAND LINE is　Less than 2 } "
argc = len(sys.argv)
argv = sys.argv
print(argc)

class Send_processing():
    def __init__(self,ip,min,max): #引数　ネットワーク接続
        self.ip = ip
        self.min = min
        self.max = max

    def tcp(self):#tcpの処理
        ip = IP(dst = self.ip)
        seq = 1000000
        for i in xrange(self.min,self.max+1):
            sport = random.randint(50000,60000)
            tcp = TCP(sport = sport,dport = i, seq = seq , flags = 'S')
            time.sleep(0.9)
            recv = sr1(ip/tcp,verbose = False,timeout=1)
            if recv == None:
                print('{0}/TCP : filtered'.format(i))
            elif recv['TCP'].flags == "SA":
                print('{0}/TCP : open'.format(i))
            elif recv['TCP'].flags == "RA":
                print('{0}/TCP : close'.format(i))

    def udp(self):
         ip = IP(dst = self.ip)
         seq = 1000000
         for i in xrange(self.min,self.max+1):
             port = i
             sport = random.randint(50000,60000)
             udp = UDP(sport = sport,dport = port)
             time.sleep(0.9)
             recv = sr1(ip/udp,verbose = False,timeout=1)
             if recv == None:
                     print('{0}/UDP : open | filtered '.format(i))
                     s = i
             elif recv['ICMP'].type ==3:
                     print('{0}/UDP : close'.format(i))
         print('open is {0}'.format(s))

    def icmp(self):
         icmp = IP(dst=self.ip)/ICMP()
         icmp.show()
         sr1(icmp)

def commandline(argc,argv): #cuiのコマンドライン実装機能 できればmanまで
    if argc >= 3:
        print(argv[1]) #3個だった場合タプルで(1,2)や(2,4)など
        return True

    elif argc <= 1 :
        print('Argument is missing - Few Argument')
        print(stment)
        return False

    elif argc > 5:
        print('Argument is missing - many Argument')
        print(stment)
        return False
    else:
        return False

def treatment_def(i,s,k,j):#Send_processingを使う
     treatment = Send_processing(i,k,j)
     if s == 1:
         treatment.tcp()
     if s == 2:
         treatment.udp()
     if s == 3:
         treatment.icmp()

def main():#通信やフレームワークなどの設定
        print(argv)
        if commandline(argc,argv):
            if argv[2] == "tcp" or argv[2] == "TCP":
                mix_ = int(argv[3])
                max_ = int(argv[4])
                if mix_ <= 65535 and mix_ > 0 and mix_ < max_ or mix_ == max_:
                        treatment_def(argv[1],1,mix_,max_)
                else:
                    print('範囲を設定してください。')

            elif argv[2] == "udp" or argv[2] == "UDP":
                mix_ = int(argv[3])
                max_ = int(argv[4])
                if mix_ <= 65535 and mix_ > 0 and mix_ < max_ or mix_ == max_:
                        treatment_def(argv[1],2,mix_,max_)
                else:
                    print('範囲を指定してくっださい。')
            elif argv[2] == "icmp" and argv[2] == "ICMP":
                if argv[3] == None and argv[4] == None:
                    treatment_def(argv[1],3,None,None)
                else:
                    print('ICMPのときは範囲をしていしなくていいです。')
        else:
            print('tcpやudpを設定してください')

if __name__ == "__main__":
    main()
