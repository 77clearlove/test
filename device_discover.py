import socket
import sys
ip = "239.255.255.250"
port = 3702

message = "<?xml version=\"1.0\" encoding=\"utf-8\"?>" \
         "<Envelope xmlns:dn=\"http://www.onvif.org/ver10/network/wsdl\" xmlns=\"http://www.w3.org/2003/05/soap-envelope\">" \
         "<Header><wsa:MessageID xmlns:wsa=\"http://schemas.xmlsoap.org/ws/2004/08/addressing\">" \
         "uuid:fc0bad56-5f5a-47f3-8ae2-c94a4e907d70</wsa:MessageID>" \
         "<wsa:To xmlns:wsa=\"http://schemas.xmlsoap.org/ws/2004/08/addressing\">" \
         "urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To>" \
         "<wsa:Action xmlns:wsa=\"http://schemas.xmlsoap.org/ws/2004/08/addressing\">" \
         "http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action>" \
         "</Header><Body><Probe xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" " \
         "xmlns=\"http://schemas.xmlsoap.org/ws/2005/04/discovery\">" \
         "<Types>dn:NetworkVideoTransmitter</Types><Scopes/></Probe></Body></Envelope>"

def getOnvifIp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp
    except socket.error, msg:
        # "Failed to create socket.Error code: " + str(msg[0]) + ", Error messgae: " + msg[1]
        sys.exit()

    # # "Socket Created"

    s.settimeout(5)

    try:
        s.sendto(message, (ip, port))
    except socket.error:
        # "Send failed!"
        sys.exit()

    # # "Message send successfully"

    l = []

    try:
        while 1:
            data = s.recvfrom(1024)
            # data[0]
            if not data: break
            l.append(data[1])
    except socket.error:
        s.close()
    return l

if __name__ == '__main__':
    print(getOnvifIp())
