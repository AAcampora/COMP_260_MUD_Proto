import socket
import time

if __name__ == '__main__':

    # check if the server is working
    isRunning = True

    # check if the server is conncected to any clients
    isConnected = False

    # create the socket and bind it to this address
    mySocket = socket.socket(socket.AFI_INET, socket.SOCK_STREAM)
    mySocket.bind(("127.0.0.1", 8222))
    mySocket.listen(5)


    while isRunning == True:

        # Case: client is not connected to server
        if isConnected == False:

            print("Waiting for client... ")
            client = mySocket.accept()

        try:
            data = client[0].recv(4096)
            print(data.decode("utf-8"))

            isConnected = True
            print("Client Sucessfuly Connected")

        except socket.error:
            isConnected = False









