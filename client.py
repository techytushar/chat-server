import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5555
host = str(input("Enter host name - "))

try:
    s.connect((host, port))
    print("Connection Established")
except:
    print("Connection Failed")
intro = "#### Welcome to the chat server. Type your message and press 'q' to quit ####"
print("\n",intro)
message = ""
while True:
    message = input("You -> ")
    if message == 'q':
        break
    s.sendall(str.encode(message))
    data = s.recv(2048)
    check = data.decode("UTF-8")
    if check == '':
        break
    print("Friend -> ",check)
print("Connection was terminated.")
s.close()
