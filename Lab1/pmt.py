import numpy as np
from array import array

def photoncount( IntTime, IntNum ):

    import socket
    #TCP_IP = '127.0.0.1'
    TCP_IP = '128.100.89.237'
    TCP_PORT = 2055
    BUFFER_SIZE = 131072
    MESSAGE="measure %f %d\n" % (IntTime,IntNum)
    bMESSAGE=MESSAGE.encode()
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(bMESSAGE)
    bReturn = s.recv(BUFFER_SIZE)
    s.close()
    sReturn = bReturn.decode()
    sReturn = sReturn.rstrip()

    #return sReturn


    sdata = sReturn.split(',')

    data = array('l')

    for x in sdata:
        if x.isdigit():
            data.append(long(x))
        else:
            print(x)
    
    
    #if sReturn.find('Error') == -1:
        
    #else:
     #   print(sReturn)
    
    return np.array(data, dtype=np.int)


def printMax ( data ):
    Max = 0
    
    for x in data:
        if x > Max:
            Max = x

    return Max
