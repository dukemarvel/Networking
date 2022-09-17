import socket

target = ' 192.168.43.206'

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.connect((target, port))
        return True

    except:
        return False

for i in range(100000, 600000):
    result = portscan(i)

    if result:
        print('Port {} is open'.format(i))

        