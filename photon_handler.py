from Db_helper import *


'''
this class handles all the different processes that should be handled
by the server. The actual server code will check to see what is passed
in and if it is info from the photons, then it will call this class to
handle the data.


This will effectively give me cleaner code that is much easier to read
and tweak.
'''

class photonHandler:

    # the format of split data:
    # ([mac address, xx:XX:xx:XX:xx],
    #  [temperature, x.xxxxxxxxxxxx],
    #  [humidity,    x.xxxxxxxxxxxx],
    #  [light,       x.xxxxxxxxxxxx],
    #  [moisture,    x.xxxxxxxxxxxx],
    #  [time,        x.xxxxxxxxxxxx])
    __split_data = None
    __db = None

    # ========================================================================================================initialize
    # init takes in nothing, and initializes the split data list
    # and the database
    def __init__(self):
        self.__split_data = []
        self.__db = DbHelper()


    # ==================================================================================================local store data
    # this function takes in the data received by the server from the
    # photon, splits it up, and locally stores it for later use
    # the passed in form:
    #                     data_label~data
    # the data is stored into split data as couples
    def local_store_data(self, data):
        # first, split up the data and then store it
        self.__split_data.append(data.split("~"))


    # =================================================================================================store to database
    # store the information that is in split data into the database
    # should be called only once, after all the data is received from
    # the photon
    def store_to_database(self):

        # first, go through the data and check what the data label is
        # for each of the different couples
        for data in self.__split_data:

            # if it is a mac address
            if data[0] == "mac address":
                # go through and check to see if the mac address is
                # is already stored in the database. if it is, then
                # that means the photon has connected to the server
                # before. IF NOT, then store the new mac address
                # and create a new row in the database for it
                if self.__db.search_for_plant(data[1]) == False:
                    self.__db.add_plant(data[1])

            # if it is not a mac address, then just store the data
            elif data[0] == "temperature" or data[0] == "humidity" or data[0] == "light" or data[0] == "moisture":
                # takes in:       type of reading,     current time stampe,     the reading,      and the mac address
                print("type: " + data[0])
                print("time: " + self.__split_data[5][1])
                print("reading: " + data[1])
                print("mac address: " + self.__split_data[0][1] + "\n")
                self.__db.add_sensor_reading(data[0], self.__split_data[5][1], data[1], self.__split_data[0][1])


        # now update the average sunlight of the plant bed associated
        # with the photon that just passed in the sensor readings
        retval =self.__db.update_plant_bed_average_sunlight(self.__split_data[0][1], self.__split_data[3][1])


        # now that all the data is stored, clear out __split_Data
        self.__split_data = []

