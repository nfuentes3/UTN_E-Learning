import socket
import datetime


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "localhost"
PORT = 12345

server_socket.bind((HOST, PORT))
server_socket.listen(5)


print("Servidor escuchando a puerto", PORT)

client_socket, addr = server_socket.accept()
print("Conexión desde", addr)


try:
    while True:
        mensaje = client_socket.recv(1024).decode()
        if not mensaje:
            print("Cliente desconectado.")
            break  # Salir del bucle si el cliente cierra la conexión
        print(mensaje)

except Exception as err:
    print("Error en el servidor:", err)

finally:
    client_socket.close()  # Cerrar la conexión con el cliente
    server_socket.close()  # Cerrar el servidor
