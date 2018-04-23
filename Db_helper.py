import os
import sqlite3
from sqlite3 import Error


class DbHelper:
    __connection_string = ""

    # ==============================================================
    def __init__(self):
        # connect to the database real quick to make sure it exist
        self.__create_connection()
        # create the tables if they do not exist
        self.__create_tables()

        print("Connected to the database")
    # ==============================================================

    # ==============================================================
    # this function creates a connection with the database and returns it
    def __create_connection(self):
        # grab the path to this file, with it
        # we have the location to safely build
        # the database.
        file = __file__
        path_with_file = os.path.realpath(file)
        directory = os.path.dirname(path_with_file)

        # now use this directory to create the database.
        # if the database already exist, then connect to it
        self.__connection_string = directory + "\plant_info.db"
    
        try:
            conn = sqlite3.connect(self.__connection_string)

            conn.commit()
            conn.close()

        except Error as e:
            print(e)
    # ==============================================================

    # ==============================================================
    # creates the tables in the database
    def __create_tables(self):
        conn = sqlite3.connect(self.__connection_string)
        cursor = conn.cursor()

        # build the strings that will be used to create the tables
        plant_bed_string = "CREATE TABLE IF NOT EXISTS Plant_beds ( "
        plant_bed_string += "plant_bed_id INTEGER PRIMARY KEY AUTOINCREMENT, "
        plant_bed_string += "name TEXT, "
        plant_bed_string += "longitude TEXT, "
        plant_bed_string += "latitude TEXT, "
        plant_bed_string += "time_zone TEXT, "
        plant_bed_string += "average_sunlight REAL );"

        plant_string = "CREATE TABLE IF NOT EXISTS Plants ( "
        plant_string += "mac_address TEXT PRIMARY KEY NOT NULL, "
        plant_string += "name TEXT, "
        plant_string += "type TEXT, "
        plant_string += "planted_date TEXT, "
        plant_string += "moisture_range TEXT NOT NULL, "
        plant_string += "heat_range TEXT NOT NULL, "
        plant_string += "light_range TEXT NOT NULL, "
        plant_string += "humidity_range TEXT NOT NULL, "
        plant_string += "plant_bed_id INTEGER );"

        sensor_string = "CREATE TABLE IF NOT EXISTS Sensor_readings ( "
        sensor_string += "sensor_id INTEGER PRIMARY KEY AUTOINCREMENT, "
        sensor_string += "type_of_reading TEXT NOT NULL, "
        sensor_string += "time_stamp TEXT NOT NULL, "
        sensor_string += "reading REAL NOT NULL, "
        sensor_string += "plant_mac_address TEXT NOT NULL );"

        try:
            #execute the creation of the tables
            cursor.execute(plant_bed_string)
            cursor.execute(plant_string)
            cursor.execute(sensor_string)

            #commit the changes to the database
            conn.commit()

            #close the connection
            conn.close()

        except Error as e:
            print(e)
    # ==============================================================

    # ==============================================================
    # adds a plant to the database
    def add_plant(self, mac_address):
        # the only required info needed for the Arduino's
        # info to be stored is its mac address

        # ADD VALIDATION OF THE MAC ADDRESS HERE LATER
        # set up the string that will be executed
        insert_string = "INSERT INTO Plants VALUES (?, NULL, NULL, NULL, ?, ?, ?, ?, NULL) "
        # insert_string += "SELECT mac_address WHERE NOT EXISTS(SELECT 1 FROM Plants WHERE mac_address = ?);"
        # create the parameter list
        params = [mac_address, "0:1", "0:1", "0:1", "0:1"]

        # execute the insert
        self.__execute_insert_query(insert_string, params)
    # ==============================================================

    # ==============================================================
    # adds / changes the name of a plant
    def name_plant(self, mac_address, name):
        # create the query
        update_string = "UPDATE Plants SET name = ? WHERE mac_address = ?"
        # create the params
        params = [name, mac_address]

        # execute the query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # changes / adds the type of the plant
    def change_plant_type(self, mac_address, plant_type):
        update_string = "UPDATE Plants SET type = ? WHERE mac_address = ?"

        params = [plant_type, mac_address]

        # execute the query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # changes / adds a date for when the plant was planted
    def change_planted_date(self, mac_address, date):
        update_string = "UPDATE Plants SET planted_date = ? WHERE mac_address = ?"

        params = [date, mac_address]

        #execute the query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # changes the moisture range
    def change_moisture_range(self, mac_address, range):
        update_string = "UPDATE Plants SET  moisture_range = ? WHERE mac_address = ?"

        params = [range, mac_address]

        # execute query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # changes the heat range
    def change_heat_range(self, mac_address, range):
        update_string = "UPDATE Plants SET heat_range = ? WHERE mac_address = ?"

        params = [range, mac_address]

        # execute the query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # changes the light range
    def change_light_range(self, mac_address, range):
        update_string = "UPDATE Plants SET light_range = ? WHERE mac_address = ?"

        params = [range, mac_address]

        # execute the query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # changes the humidity range
    def change_humidity_range(self, mac_address, range):
        update_string = "UPDATE Plants SET humidity_range = ? WHERE mac_address = ?"

        params = [range, mac_address]

        # execute the query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # links a plant to one of the existing plant beds
    def link_plant_to_bed(self, plant_bed_id, mac_address):
        update_string = "UPDATE Plants SET plant_bed_id = ? WHERE mac_address = ?"

        params = [plant_bed_id, mac_address]

        # execute query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # unlinks a plant from the plant bed it was linked too
    def unlink_plant_from_bed(self, mac_address):
        update_String = "UPDATE Plants SET plant_bed_id = NULL WHERE mac_address = ?"

        param = [mac_address]

        # execute the query
        self.__execute_insert_query(update_String, param)
    # ==============================================================

    # ==============================================================
    # searches through the database to see if the plant
    # already exist
    def search_for_plant(self, mac_address):

        ret_val = False
        # create the search string
        search_string = "SELECT * FROM Plants WHERE mac_address = ?;"
        params = [mac_address]

        # execute the search
        rows = self.__execute_search_query(search_string, params)

        # if the rows list is empty, that means
        # that plant is not yet stored in the database
        # this checks to see if the rows list is empty
        if rows:
            # if it isn't empty return true
            ret_val = True

        #return ret_val
        return ret_val
    # ==============================================================

    # ==============================================================
    # creates a new plant bed
    # returns the id of the newly created bed
    def create_plant_bed(self, name, longitude, latitude, time_zone):
        insert_string =  "INSERT INTO Plant_beds(name, longitude, latitude, time_zone, average_sunlight) VALUES (?, ?, ?, ?, ?);"

        params = [name, longitude, latitude, time_zone, "NULL"]

        # execute query
        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(insert_string, params)
            plant_bed_id = cursor.lastrowid
            # comit the insert
            conn.commit()

            # close the connection
            conn.close()
            return plant_bed_id
        except Error as e:
            print(e)
    # ==============================================================

    # ==============================================================
    # change the plant bed name
    def change_plant_bed_name(self, plant_bed_id, name):
        update_string = "UPDATE Plant_beds SET name = ? WHERE plant_bed_id = ?"

        params = [name, plant_bed_id]

        # execute the query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # changes the location of the plant bed
    def change_plant_bed_location(self, plant_bed_id, longitude, latitude):
        update_string = "UPDATE Plant_beds SET longitude = ?, latitude = ? WHERE plant_bed_id = ?"

        params = [longitude, latitude, plant_bed_id]

        # execute the query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # changes the time zone of a plant bed
    def change_plant_bed_time_zone(self, plant_bed_id, time_zone):
        update_string = "UPDATE Plant_beds SET time_zone = ? WHERE plant_bed_id = ?"

        params = [time_zone, plant_bed_id]

        # execute the query
        self.__execute_insert_query(update_string, params)
    # ==============================================================

    # ==============================================================
    # updates the average sunlight for a plant bed
    # takes in the current photon's mac address that just send sensor
    # data and the light value it just sent
    def update_plant_bed_average_sunlight(self, plant_mac, light):             # TEST THIS SHIT ASAP SDL;KFJA;LSKDJFLA;KSDJF;LAKSJDF;LASKJDF;LKASJDF;
        # 1st query for the plant bed associated with the passed in
        # mac address. (FROM Plants, WHERE mac_address = plant_mac)
        # construct the query string for the plant table
        find_plant_bed_id = "SELECT DISTINCT plant_bed_id FROM Plants WHERE mac_address = ?"
        param = [plant_mac]

        # construct the query string for the plant bed table
        find_average_sunlight = "SELECT average_sunlight FROM Plant_beds WHERE plant_bed_id = ?"

        # construct the update query string
        update_string = "UPDATE Plant_beds SET average_sunlight = ? WHERE plant_bed_id = ?"

        # open a connection and preform the queries
        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            # execute the query to find the plant bed id
            # there should only be one row since we are only
            # grabbing the plant bed id
            cursor.execute(find_plant_bed_id, param)
            plant_bed_id = cursor.fetchone()
            # reassign what the parameter is to be passed in for the next query
            param = [plant_bed_id[0]]

            # if the first query did find a plant bed that the plant is linked to
            if plant_bed_id[0] != None:
                # now preform the 2nd query to find the average sunlight
                # based on the found plant bed id
                cursor.execute(find_average_sunlight, param)
                average_sunlight = cursor.fetchone()

                # close the connection for now with the db
                conn.close()

                average_sunlight = float(average_sunlight[0])
                # now check the value of the average sunlight for the plant bed
                # if it is zero, then this is a new plant bed just recently created
                # by the user. so just assign the new light value to the average sunlight
                if average_sunlight == None:
                    # reassign the param to be passed in with the update query
                    param = [light, plant_bed_id[0]]

                    # execute the update query
                    self.__execute_insert_query(update_string, param)


                elif average_sunlight >= 0:
                    # find the new average sunlight
                    new_average = average_sunlight + light
                    new_average = new_average / 2.0

                    print("average sunlight: " + str(new_average))

                    # reassign the param to be passed in with the update query
                    param = [new_average, plant_bed_id[0]]

                    # execute the update query
                    self.__execute_insert_query(update_string, param)

                    # return TRUE if update was successful
                    return True

            # the first query found no linked plant beds
            else:
                conn.close()
                return False

        except Error as e:
            print("\n" + str(e) + "\n")
    # ==============================================================

    # ==============================================================
    # adds all the sensor readings from the Arduino
    # takes =======================================================
    # returns a string containing all the plant bed names
    def get_plant_bed_names(self):
        # construct the query strings
        plant_bed_String = "SELECT name, plant_bed_id  FROM Plant_beds"

        # open a connection and preform the query
        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(plant_bed_String)

            #grab the rows of the plant bed names
            bed_rows = cursor.fetchall()

            # close the connection
            conn.close()

            # return the rows found
            return bed_rows

        except Error as e:
            print(e)

    # ==============================================================
    # ==============================================================
    # returns a dictionary of all of the data
    # from the plant anin a list of the information about the photon: mac address,
    # temperature, humidity, light, moisture, and time stamp.
    def add_sensor_reading(self, type, time_stamp, reading, mac):
        insert_string = "INSERT INTO Sensor_readings(type_of_reading, time_stamp, reading, plant_mac_address) VALUES(?, ?, ?, ?);"

        params = [type, time_stamp, reading, mac]

        # execute query
        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(insert_string, params)
            plant_bed_id = cursor.lastrowid
            # comit the insert
            conn.commit()

            # close the connection
            conn.close()
            return plant_bed_id
        except Error as e:
            print("\n" + e + "\n")
    # ==============================================================

    # ==============================================================
    # grabs all the data related to one plant bed (plant bed info
    # and all of the plants related to the bed + their info) used for
    # the tables so that the VURA can use it
    def get_plant_and_bed_data(self, plant_Bed_id):
        # construct the query strings
        plant_string = "SELECT * FROM Plants WHERE plant_bed_id = ?"

        bed_string =  "SELECT * FROM Plant_beds WHERE plant_bed_id = ?"

        params = [plant_Bed_id]

        # open a connection and preform both queries
        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(plant_string, params)
            # grab the rows for the plants
            plant_rows = cursor.fetchall()
            # ----------------------------------
            cursor.execute(bed_string, params)
            # grab the rows for the beds
            bed_rows = cursor.fetchall()

            # close the connection
            conn.close()


            # create a list size 2 with each element being a row
            info = [plant_rows, bed_rows]

            return info
        except Error as e:
            print(e)
    # ==============================================================

    # ==============================================================
    # this function grabs the plants that are not linked to any of
    # the plant beds. They should be presented in a menu
    def get_lost_plants(self):

        # construct the query string
        plant_string = "SELECT * FROM Plants Where plant_bed_id IS NULL"


        # open a connection and preform the query
        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            # execute the query
            cursor.execute(plant_string)

            # grab all the rows returned
            plant_rows = cursor.fetchall()

            # close the connection
            conn.close()

            return plant_rows
        except Error as e:
            print(e)
    # ==============================================================

    # ==============================================================
    # executes a query on the database based off
    # of the query string passed in and parameters.
    # It executes the insert and returns a
    # connection object so that the connection
    # doesn't have to be closed in this function
    def __execute_insert_query(self, query_string, params):
        try:
            # connect to the database anc create a cursor
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            # use the cursor to execute the query
            cursor.execute(query_string, params)

            # commit the insert
            conn.commit()

            # close the connection
            conn.close()

        except Error as e:
            print(e)
    # ==============================================================

    # ==============================================================
    # takes in a search string and parameters and
    # searches the database for the passed in info.
    # returns the rows of what it finds
    def __execute_search_query(self, query_string, params):
        try:
            # connect to the database anc create a cursor
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            # use the cursor to execute the query
            cursor.execute(query_string, params)

            # commit the insert
            conn.commit()

            # grab the rows returned from the query
            rows = cursor.fetchall()

            # close the connection
            conn.close()

            # return the rows
            return rows
        except Error as e:
            print(e)
    # ==============================================================