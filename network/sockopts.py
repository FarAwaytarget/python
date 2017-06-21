import socket, traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
print "waiting for connections....."
s.listen(1)
while 1:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        print traceback.print_exc()
        continue
    # process the connection
    try:
        print "got connection from", clientsock.getpeername()
        # process the request here

    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

    print "got connection from", clientsock.getpeername
    # close the connection
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()