import socket
import sys
from photon_handler import *
from oculus_handler import *

# create the photon handler
photon = photonHandler();

# create the oculus handler
oculus = oculusHandler();



# beds = oculus.get_plant_bed_names()


# grab the host name so that I can grab the ip address
IP = socket.gethostbyname(socket.gethostname())
PORT = 8080


# create a TCP / IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host host and a port
server_socket.bind((IP, PORT))


# =============================================================================================================functions
def check_data(client_connection, return_data):
    # check the size of the data list

    # -------------------------------------------photon-----------------------------------------------------------------
    # if it is 6 long, then it was a photon
    # that connected to the server
    if len(return_data) == 6:
        # go through the data snet by the photon
        for data in return_data:
            # locally store the data
            photon.local_store_data(data)

        # once all the data has been processed,
        # store it to the database
        photon.store_to_database()
    # ------------------------------------------------------------------------------------------------------------------

    # -------------------------------------------oculus-----------------------------------------------------------------

    # when the user starts the oculus rift application, Go and grab
    # all of the plant bed names as well as their IDs
    elif len(return_data) == 1 and return_data[0] == "log on":
        print("CHOKE UP ON THE CLUB!!!!!!")
        # grab the plant bed data from the database
        send_string = oculus.get_plant_bed_names()
        print(send_string)
        # encode the string being sent and send it
        client_connection.send(send_string.encode('ascii'))

    # if the data sent by the oculus rift is the selected
    # plant bed's id
    elif len(return_data) == 1 and 'bed_id' in return_data[0]:

        # first seperate the data string to grab the id
        bed_id = return_data[0].split(": ")
        oculus.get_plant_beds_plant_data(int(bed_id[1]))
    # ------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================














# this function begins to listen for connections made by either
# the Oculus rift or the photons. It returns an array of the
# data that was sent through the pipe
#def listen(socket):

# ------------------------------------- main ---------------------------------------------------------------------------
# tell the socket to listen
# allows up to 5 queued connections
server_socket.listen(5)

while True:
    # print out that we are listening
    print("                                            listening on:")
    print("                                                 IP:   " + IP)
    print("                                                 PORT: " + str(PORT))

    # accept connections from outside
    (connection, client_address) = server_socket.accept()
    print("\nconnected to: ", client_address)

    # create a list that will hold the data collected
    # from the connected devices
    data = []

    # a boolean to represent if the socket is listening
    is_listening = True

    while True:
        # listening loop
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

                print ("this is data" + str(data))
                check_data(connection, data)


            # if b'' that means that the buffer is empty
            elif received == b'':
                break


        # if there is an error, then print what the error is
        except socket.error as e:
            print(e)

    print("\n\n\n")


