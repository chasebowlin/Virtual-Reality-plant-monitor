import os
import sqlite3
from sqlite3 import Error
from Validator import *


class Db_helper:
    __connection_string = ""
    __validate = Validator()

    #============================================================================================
    def __init__(self):
        self.__create_connection()
        self.__create_tables()
        print("\nconnected to database\n")
    #============================================================================================

    #============================================================================================
    def __create_connection(self):
        """grab the path to this file
            with that, create a database
            file in the same directory
            of this file
        """
        file = __file__
        path_with_file = os.path.realpath(file)
        directory = os.path.dirname(path_with_file)

        """now connect to the database
            if the database does not exist
            then create it
        """
        self.__connection_string = directory + "\plant_info.db"

        try:
            conn = sqlite3.connect(self.__connection_string)
        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def __create_tables(self):
        conn = sqlite3.connect(self.__connection_string)
        cursor = conn.cursor()

        #first check to see if the tables already exist

        #build the strings that will be used to create the tables
        plant_bed_string = "CREATE TABLE IF NOT EXISTS Plant_beds ( "
        plant_bed_string += "plant_bed_id INTEGER PRIMARY KEY AUTOINCREMENT, "
        plant_bed_string += "name Text, "
        plant_bed_string += "location TEXT, "
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

            #close the connection with the database
            conn.close()
        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def add_plant(self, mac_address):
        """the only required info needed for the Arduino's info
        to be stored is its mac address
        """
        #validate that it is a correct mac address
        if self.__validate.check_mac_address(mac_address):
            insert_string = "INSERT INTO Plants VALUES (?, NULL, NULL, NULL, ?, ?, ?, ?, NULL);"

            params = [mac_address, "0:1", "0:1", "0:1", "0:1"]
            try:
                conn = sqlite3.connect(self.__connection_string)
                cursor = conn.cursor()

                cursor.execute(insert_string, params)
                #commit the insert
                conn.commit()

                #close the connection
                conn.close()

            except Error as e:
                print(e)

        else:
            return "not a valid mac address"
    #============================================================================================

    #============================================================================================
    def add_sensor_reading(self, type_of_reading, time_stamp, reading, mac_address):
        """create the string used to insert into the sensor_readings table"""
        insert_string = "INSERT INTO Sensor_readings (type_of_reading, time_stamp, reading, plant_mac_address) VALUES (?, ?, ?, ?);"

        params = [type_of_reading, time_stamp, reading, mac_address]

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(insert_string, params)

            #commit the insert
            conn.commit()

            #close connection
            conn.close()

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def create_plant_bed(self, name, location, average_sunlight):
        #this function returns the plant bed id
        insert_string = "INSERT INTO Plant_beds(name, location, average_sunlight) VALUES (?, ?, ?);"

        params = [name, location, average_sunlight]



        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(insert_string, params)
            plant_bed_id = cursor.lastrowid
            #comit the insert
            conn.commit()

            #close the connection
            conn.close()
            return plant_bed_id
        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def change_plant_bed_name(self, plant_bed_id, name):
        update_string = "UPDATE Plant_beds SET name = ? WHERE plant_bed_id = ?"

        params = [name, plant_bed_id]
        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(update_string, params)

            #commit the changes
            conn.commit()

            #close the connection
            conn.close()
        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def change_plant_bed_location(self, plant_bed_id, location):
        update_string = "UPDATE Plant_beds SET location = ? WHERE plant_bed_id = ?"

        params = [location, plant_bed_id]

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(update_string, params)

            #commit the changes
            conn.commit()

            #close the connection
            conn.close()

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def name_plant(self, mac_address, name):
        update_string = "UPDATE Plants SET name = ? WHERE mac_address = ?"

        params = [name, mac_address]

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(update_string, params)

            #commit the changes
            conn.commit()

            #close the connection
            conn.close()

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def change_plant_type(self, mac_address, type):
        update_string = "UPDATE Plants SET type = ? WHERE mac_address = ?"

        params = [type, mac_address]

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(update_string, params)

            # commit the changes
            conn.commit()

            # close the connection
            conn.close()

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def change_planted_date(self, mac_address, date):
        update_string = "UPDATE Plants SET planted_date = ? WHERE mac_address = ?"

        params = [date, mac_address]

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(update_string, params)

            # commit the changes
            conn.commit()

            # close the connection
            conn.close()

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def change_moisture_range(self, mac_address, range):
        update_string = "UPDATE Plants SET  moisture_range = ? WHERE mac_address = ?"

        params = [range, mac_address]

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(update_string, params)

            # commit the changes
            conn.commit()

            # close the connection
            conn.close()

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def change_heat_range(self, mac_address, range):
        update_string = "UPDATE Plants SET heat_range = ? WHERE mac_address = ?"

        params = [range, mac_address]

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(update_string, params)

            # commit the changes
            conn.commit()

            # close the connection
            conn.close()

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def change_light_range(self, mac_address, range):
        update_string = "UPDATE Plants SET light_range = ? WHERE mac_address = ?"

        params = [range, mac_address]

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(update_string, params)

            # commit the changes
            conn.commit()

            # close the connection
            conn.close()

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def change_humidity_range(self, mac_address, range):
        update_string = "UPDATE Plants SET humidity_range = ? WHERE mac_address = ?"

        params = [range, mac_address]

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(update_string, params)

            # commit the changes
            conn.commit()

            # close the connection
            conn.close()

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def link_plant_to_bed(self, plant_bed_id, mac_address):
        update_string = "UPDATE Plants SET plant_bed_id = ? WHERE mac_address = ?"

        params = [plant_bed_id, mac_address]

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute(update_string, params)

            # commit the changes
            conn.commit()

            # close the connection
            conn.close()

        except Error as e:
            print(e)
    #============================================================================================

    #these functions are used by the VRUA when it first connects
    #to the server
    #============================================================================================
    def get_plant_beds(self):

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Plant_beds")

            #grab the rows from the cursor
            rows = cursor.fetchall()

            conn.close()
            return rows

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def get_plants(self):

        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Plants")

            #grab the rows from the cursor
            rows = cursor.fetchall()

            conn.close()
            return rows

        except Error as e:
            print(e)
    #============================================================================================

    #============================================================================================
    def get_sensor_readings_for_plant(self, mac_address):
        try:
            conn = sqlite3.connect(self.__connection_string)
            cursor = conn.cursor()


            cursor.execute("SELECT * FROM Sensor_readings WHERE plant_mac_address = ?", [mac_address])


            #grab the rows from the cursor
            rows = cursor.fetchall()

            conn.close()
            return rows

        except Error as e:
            print(e)
    #============================================================================================

