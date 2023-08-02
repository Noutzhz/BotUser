import socket

server_ip = "localhost"
port = 7658
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server_ip, port))
s.listen(5)
clients = []
print("Waiting for connections!")

def send_msg(msg):
    for client in clients:
        client.send(bytes(f"{str(msg)}", "utf-u"))
    print(f"Sent to all clients!")

while True:
    cleint, ip = s.accept()
    clients.append(client)
    messsage = input("Enter message: ")
    send_msg(msg=menssage)
