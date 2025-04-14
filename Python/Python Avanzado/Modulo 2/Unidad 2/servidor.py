import socket

mi_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mi_server.bind(("localhost", 8000))
mi_server.listen(5)


print("Esperando conexión en el puerto 8000")


cliente, address = mi_server.accept()
print(f"Conexión establecida con {address}")

mensaje = cliente.recv(1024).decode()
print(f"Mensaje recibido: {mensaje}")


cliente.close()
mi_server.close()
