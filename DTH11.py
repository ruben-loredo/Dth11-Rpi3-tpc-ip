import socket
import time
import Adafruit_DHT
socket_s = socket.socket()
host = ''
port = 9999
backlog = 5
socket_s.bind ((host,port))
socket_s.listen(backlog)
print "Esperando Conexion ..... "
socket_s, (host,port) = socket_s.accept()
print "Conexion extablecida ..... "
while True:
    humedad, temperatura = Adafruit_DHT.read_retry(11, 27)
    try:
        if(temperatura > 0):
                        sTem = (" T= {}".format(temperatura))
        if(humedad  > 0):
                        sHum = (" H= {}".format(humedad))
        socket_s.send(sTem + " " + sHum)
        time.sleep(.01)
    except:
        print "Desconectado ....."
        socket_s.close()
        break

