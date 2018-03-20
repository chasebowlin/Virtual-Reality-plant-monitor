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

        print("\nConnected to the database\n")
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
        plant_bed_string += "average_sunlight TEXT );"

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
    def create_plant_bed(self, name, longitude, latitude, time_zone, average_sunlight):
        insert_string =  "INSERT INTO Plant_beds(name, longitude, latitude, time_zone, average_sunlight) VALUES (?, ?, ?, ?, ?);"

        params = [name, longitude, latitude, time_zone, average_sunlight]

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
    # adds all the sensor readings from the Arduino
    # takes in a list of the information about the photon: mac address,
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
    # returns a dictionary of all of the data
    # from the plant and plant bed
    # tables so that the VURA can use it
    def get_plant_and_bed_data(self):
        # construct the query strings
        plant_string = "SELECT * FROM Plants"
        bed_string =  "SELECT * FROM Plant_beds"

        # open a connection and preform both queries
        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(plant_string)
            # grab the rows for the plants
            plant_rows = cursor.fetchall()
            # ----------------------------------
            cursor.execute(bed_string)
            # grab the rows for the beds
            bed_rows = cursor.fetchall()

            #close the connection
            conn.close()


            # create a dictionary to store the data
            info = {'plants': plant_rows, 'beds': bed_rows}

            return info
        except Error as e:
            print(e)
    # ==============================================================

    # ==============================================================
    # this function takes in all of the data for all the sensor
    # and stores them into the sensor reading data table
    # def store_sensor_data
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