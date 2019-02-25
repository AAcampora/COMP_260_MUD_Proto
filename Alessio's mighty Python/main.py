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

    # check if the server is working
    isRunning = True

    # check if the server is conncected to any clients
    isConnected = False

    seqID = 0

    # create the socket and bind it to this address
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #mySocket.bind(("127.0.0.1", 8222))
    mySocket.listen(5)


    while isRunning == True:

        # Case: client is not connected to server
        if isConnected == False:

            print("Waiting for client... ")
            client = mySocket.accept()

        try:
            data = client[0].recv(4096)
            print(data.decode("utf-8"))
            seqID = 0
            isConnected = True
            print("Client Sucessfuly Connected")

        except socket.error:
            isConnected = False

        while isConnected == True:

            testString = str(seqID) +":" + time.ctime()

            try:
                print("Sending test String: " + testString)
                client[0].send(testString.encode())
                seqID += 1
                time.sleep(0.5)
            except socket.error:
                isConnected = False
                client = None
                print("Client Lost")










