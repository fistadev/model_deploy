import socket
import numpy as np
from model import X_test


#lst = [5.1, 3.5, 1.4, 0.2]
#a = np.array(X_test)
#a = a.tobytes()


def client():
    HOST = '127.0.0.1'
    PORT = 5010
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print('Client connected.')
    while True:
        user_input = str(input(X_test))
        if user_input == "exit":
            break
        mess = user_input.encode()
        s.sendall(mess)

    return s
