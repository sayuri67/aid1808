# server.py
import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('0.0.0.0', 8080))

phone.listen(5)

print('starting....')
conn, addr = phone.accept()
print(conn)
print('client addr', addr)
print('ready to read msg')
client_msg = conn.recv(1024)
print('client msg: %s' % client_msg)
conn.send(client_msg.upper())

conn.close()
phone.close()
