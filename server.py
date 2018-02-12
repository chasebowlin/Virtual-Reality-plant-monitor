from Db_helper import *
from Validator import *
"""create the database"""
database = Db_helper()

#database.add_plant("12:11:10:09:08:07")
#database.get_plant()
#database.add_sensor_reading("temperature", "02:12:1996:12:12:12", 12.234, "12:11:10:09:08:07")
#id = database.create_plant_bed("death", "hell", "not enough")

#database.change_plant_bed_name(id, "heaven")
#database.change_plant_bed_location(id, "in the clouds")

#database.name_plant("12:11:10:09:08:07", "way of life")
#database.name_plant("test", "never gunna give you up")
#database.change_plant_type("test", "a true test should break")
#database.change_planted_date("test", "yesterday duh")
#database.change_moisture_range("test", "1:232.345")
#database.change_heat_range("test", "2.3:34")
#database.change_light_range("test", "no light: too much light")
#database.change_humidity_range("test", "1:12345678")
#database.link_plant_to_bed(22, "test")

#readings = database.get_sensor_readings_for_plant("test")
#data = database.get_sensor_readings_for_plant("12:11:10:09:08:07")

#for row in data:
 #   print(row)

#plant_beds = database.get_plant_beds()
#plants = database.get_plants()


#TEST THE VALIDATOR
validation = Validator()
test = validation.check_planted_date("02/29/1900")
print(test)

test = validation.check_range("12322.68987:9478")

print(test)

test = validation.check_mac_address("02:12:A0:12:12:12")

print(test)

