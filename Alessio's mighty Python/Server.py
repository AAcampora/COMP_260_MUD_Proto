import socket
import time
import threading

clients = {}
clientsLock = threading.Lock()


def acceptThread(serverSocket):
    while True:
        new_client = serverSocket.accept()
        print("Added Client")
        clientsLock.acquire()
        clients[new_client[0]] = 0
        clientsLock.release()


if __name__ == '__main__':

    # create the socket and bind it to this address
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind(("127.0.0.1", 8222))
    mySocket.listen(5)

    myThread = threading.Thread(target=acceptThread, args=(mySocket, ))
    myThread.start()

    while True:
        lostclients = []


        clientsLock.acquire()
        for client in clients:
            try:
                data = client.recv(4096).decode()

                user_input = data.split(' ')

                user_input = [x for x in user_input if x != '']

                if user_input[0].lower() == 'hi':

                    stringToSend = "Hi :D how are you?"


            except socket.error:
                lostclients.append(client)
                print("Lost client!")

        for client in lostclients:
            clients.pop(client)

        clientsLock.release()

        time.sleep(0.5)

