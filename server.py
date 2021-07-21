import socket
import os
import pickle
import numpy as np

# load the model from disk


# def load_model():
#     filename = 'iris_model.pkl'
#     loaded_model = pickle.load(open(filename, 'rb'))
#     return loaded_model


# model = load_model()


def server():
    HOST = '88.1.56.23'
    PORT = 5011

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP SOCKET
    s.bind((HOST, PORT))
    while True:
        s.listen(1)
        conn, addr = s.accept()
        print('Client connected: ', addr)

        while True:
            data = conn.recv(1024)
            received = np.frombuffer(data)
            #received = received.reshape(-1, 1)
            print(received)
            # pred = model.predict(received)
            # if not data or data == "":
            #     break
            # decoded_data = data.decode()
            # print(decoded_data)

            # print(pred)
            # return pred
            return received


    # return decoded_data
server()
