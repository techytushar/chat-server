import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5555
host = ''
try:
    s.bind((host,port))
    print("Binding Done!")
except:
    print("Binding Error.")
print("Connect to - ",socket.gethostname())
s.listen(5)
print("Waiting for connection...")
conn, addr = s.accept()
print("Connection Established with -> ", addr,"\n")
intro = "#### Welcome to the chat server. Type your message and press 'q' to quit ####"
print("\n",intro)

while True:
    data = conn.recv(2048)
    if not data:
        break
    message = data.decode("UTF-8")
    print("Friend -> ",message)
    reply = input("You -> ")
    if reply == 'q':
        break
    conn.sendall(str.encode(reply))
print("Connection was terminated")
conn.close()



