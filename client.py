import socket
import numpy as np
# from model import X_test


lst = [5.1, 3.5, 1.4, 0.2]
a = np.array(lst)
a = a.tobytes()


def client():
    HOST = '88.1.56.23'
    PORT = 5011
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print('Client connected.')
    while True:
        user_input = str(input())
        if user_input == "exit":
            break
        mess = user_input.encode()
        s.sendall(a)

    return s
