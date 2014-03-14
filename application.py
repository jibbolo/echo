from socket import *
    
if __name__=='__main__':
    HOST = '0.0.0.0'
    PORT = 5555
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind(ADDR)
    serversock.listen(2)
    while 1:
        try:
            print 'waiting for connection...'
            clientsock, addr = serversock.accept()
            print '...connected from:', addr
            while 1:
                data = clientsock.recv(BUFSIZ)
                if data.strip() == "quit":
                    break
                msg = 'echoed:... ' + data
                clientsock.send(msg)
            clientsock.close()
            
        except KeyboardInterrupt:
            print "exiting.."
            serversock.close()
            break