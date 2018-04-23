from Db_helper import *
from sun_position import *

'''
This class handles all the request that are made by the oculus rift
application. The main server code will check to see what commands
were sent over the data stream and then call the specific function
from oculus_handler
'''


class oculusHandler:

    # this data member will hold the connection to the database
    __db = None

    # a dictionary that maps all the USA time zones with their
    # offset from UTC.
    __UTC_offset_dictionary = { 'AST': -4,
                                'EST': -5,
                                'CST': -6,
                                'MST': -7,
                                'PST': -8,
                                'AKST': -9,
                                'HST': -10}


    # ========================================================================================================initialize
    # init takes in nothing, and initializes the connection to the database
    def __init__(self):
        self.__db = DbHelper()


    # ===============================================================================================get plant bed names
    # go and grab all the names of the different plant beds
    # also grabs the ids of the plant beds
    def get_plant_bed_names(self):
        # connect to the database, grab the list of all
        # of the plant beds
        plant_beds = self.__db.get_plant_bed_names()

        # return string
        ret_val = ""

        # now convert the couples into one long string
        # that we can send back to the oculus
        for data in plant_beds:
            ret_val += data[0] + ":" + str(data[1]) + "~!~"

        # return the string of plant bed names + ids
        return ret_val

    # =========================================================================================get plant beds plant data
    # this function grabs all of the data about the passed in plant bed
    # and all the plants associated to the plant bed.
    # this function also calculates the position of the sun
    # plant_bed_id == int
    def get_plant_beds_plant_data(self, plant_bed_id):

        bed_data = plant_Bed_info = self.__db.get_plant_and_bed_data(plant_bed_id)

        # should construct a string so that we can send it through the data stream