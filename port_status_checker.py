# Port Status Checker
# Checks whether a port is open on your own computer (localhost).

import socket

port_text = input("Enter the port number to check: ")

if not port_text.isdigit():
    print("Invalid input. Please enter a number.")
else:
    port = int(port_text)

    if port < 1 or port > 65535:
        print("Invalid port. Enter a number from 1 to 65535.")
    else:
        host = "127.0.0.1"  # Your own computer
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            print("Port", port, "is OPEN on your computer.")
        else:
            print("Port", port, "is CLOSED or not accepting connections.")
