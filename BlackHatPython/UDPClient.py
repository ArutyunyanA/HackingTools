import socket


def main(target_host, target_port):
    # create a socket object by using IPv4 address 
    # as AF_INET and SOCK_DGRAM indicates that we are 
    # useing UDP client 
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # send some data
    client.sendto(b'AAABBBCCC',(target_host, target_port))
    # receiev UDP data back
    data, addr = client.recvfrom(4096)
    print(data.decode())
    client.close()

if __name__ == '__main__':
    main('127.0.0.1', 9997)