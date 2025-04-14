import socket

mi_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mi_cliente.connect(("localhost", 8000))

mi_cliente.send("Hola, soy el cliente".encode())

mi_cliente.close()
