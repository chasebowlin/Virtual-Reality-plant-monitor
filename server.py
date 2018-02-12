import socket
import sys
from Db_helper import *

# on start up of the server, create the database object
db = DbHelper()


# grab the host name so that I can grab the ip address
IP = socket.gethostbyname(socket.gethostname())
PORT = 8080


# create a TCP / IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host host and a port
server_socket.bind((IP, PORT))




# this function begins to listen for connections made by either
# the Oculus rift or the photons. It returns an array of the
# data that was sent through the pipe
def listen(socket):
    # tell the socket to listen
    # allows up to 5 queued connections
    server_socket.listen(5)

    # print out that we are listening
    print("listening on: \n    IP:   " + IP + "\n    PORT: " + str(PORT))

    # accept connections from outside
    (connection, client_address) = server_socket.accept()
    print("\nconnected!")

    # create a list that will hold the data collected
    # from the connected devices
    data = []

    # a boolean to represent if the socket is listening
    is_listening = True
    # listening loop
    while is_listening:

        try:
            # this is a buffer that gathers data from the
            # socket. After the data is received, decode
            # it and make it something readable. Print
            # the data to the console for but testing
            received = connection.recv(2048)

            # check to make sure that socket connection
            # has not broken
            if received != b'':
                # append the received data onto the list
                data.append(received.decode('utf-8'))

            else:
                return data

        # if there is an error, then print what the error is
        except socket.error as e:
            print(e)

        finally:
            # clean up the connection and close it
            server_socket.close()



# main while loop
while True:
    return_data = listen(server_socket)
    # ------------------------------------------------------------------------------------------------------------------
    # check the size of the data list
    # if it is l ong, then it was a photon
    # that connected to the server
    if len(return_data) == 6:
        split_data = []
        # go through the data sent by the photon
        for data in return_data:
            # split up the list so that the data can be grabbed
            split_data.append(data.split("~"))

        # go through the list of couples and add the information about
        # the plant if it does not already exist. also add all of the
        # sensor readings
        for data in split_data:
            # print the data out to make sure that
            # it matches up with what the photon is emitting
            print(data[0] + ": " + data[1])

            # check to see if the photon's address is already linked to a plant
            if data[0] == "mac address":
                #if it is not, then add it to the database
                if db.search_for_plant(data[1]) == False:
                    db.add_plant(data[1])

            elif data[0] == "temperature" or data[0] == "humidity" or data[0] == "light" or data[0] == "moisture":
                db.add_sensor_reading(data[0], split_data[5][1], data[1], split_data[0][1])
    # ------------------------------------------------------------------------------------------------------------------

