# script Title: send packets to a samp server and print the result
# script Author: Cartter#0001
# Vendor Homepage:  https://www.sa-mp.com/
# Version: 0.3.7-R4 
# Tested on: 0.3.7-R4

import socket, codecs
import argparse

def encode(cmd):
    while True:
        encode = cmd.encode()
        try:
            encode = codecs.decode(cmd, "hex_codec")
        except:
            encode = cmd.encode()
        break
    return encode


def exec_cmd(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        cmd = input(">>>")
        if (cmd != 'exit'):

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

            sock.sendto(encode(cmd), (target, int(port)))
            sock.settimeout(2)

            try:
                len = sock.recv(4096)
                print(len, end='\n')

            except Exception as e:
                print(e, end='\n')
        else:
            exit(0)

def main():
    parser = argparse.ArgumentParser(description="samp packet test")
    parser.add_argument(
        '-t', '--target', help='Specify the IP', required=True)

    parser.add_argument(
            '-p', '--port', help='Specify the PORT', required=True)

    arg = parser.parse_args()

    try:
        exec_cmd(arg.target, arg.port)
    except KeyboardInterrupt:
        exit(1)
    except EOFError:
        exit(1)

if __name__ == '__main__':
    main()