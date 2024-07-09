import socket


def main(target_host, target_port):
    # create a socket object by using IPv4 address or 
    # hostname as AF_INET and SOCK_STREAM indicates 
    # that it will be a TCP client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the client by pass our variables
    client.connect((target_host, target_port))
    # send some data as bytes
    client.send(b'GET / HTTP/1.1\r\nHost: some_dns_name.com\r\n\r\n')
    # receive some data
    response = client.recv(4096)
    # print out of response
    print(response.decode())
    client.close()

if __name__ == '__main__':
    main('0.0.0.0', 9998)