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
    def tcp():#tcpの処理
        ip = IP(dst = self.ip)
        tcp = TCP(sport = sport,dport = self.port, seq = seq , flags = 'S')
        recv = sr1(ip/tcp)
        print(recv)


def commandline(argc,argv): #cuiのコマンドライン実装機能 できればmanまで
    if argc == 2:
        print('To start the communication') #3個だった場合タプルで(1,2)や(2,4)など
        return True

    elif argc <= 1 :
        print('Argument is missing - Few Argument')
        print(stment)
        return False

    elif argc >= 3:
        print('Argument is missing - many Argument')
        print(stment)
        return False

        def certify():
            if commandline():
                # if argv[2] is #きまったら処理　自分としては -s 探す　-v　見る　-
                pass
            # elif commandline() == 0:
            #     print()

def treatment():#Send_processingを使う
     treatment = Send_processing()
     treatment.tcp(localhost,1234)

def main():#通信やフレームワークなどの設定
    pass

if __name__ == "__main__":
    commandline(argc,argv)
