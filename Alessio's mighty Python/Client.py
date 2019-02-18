import socket
import time

#Client Side

# start of the application
if __name__ == '__main__':

    # checks if the server is connected to a client
    isConnected = False

    # contains the socket data
    mySocket = None

    # checks if the Server is currently running
    isRunning = True

    while isRunning == True:

        while isConnected == False:

            # if by case the socket was not created
            if mySocket is None:
                mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # check if the server is connected
            try:
                mySocket.connect(("127.0.0.1", 8222))
                isConnected = True
            except socket.error:
                isConnected = False
                print("Socket not made")

            # check if the socket is connected
            if(isConnected == True):
                try:
                    testString = "Connected to Server"
                    mySocket.send(testString.encode())

                except:
                    isConnected = False
                    mySocket = None

                    if isConnected == False:
                        print("Server not Found")
                        time.sleep(1.0)

        # when the server is connected to the client
        while isConnected == True:
            # check if the server has lost connection
            try:
                data = mySocket.recv(4096)
                print(data.decode("utf-8"))
            except:
                isConnected = False
                mySocket = False
                print("Server Lost")


