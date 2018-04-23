import math



class sunPosition:
    # used to find many other elements for the sun
    __decimal_hour = 0
    __decimal_day = 0
    __obliquity_of_the_ecliptic = 0

    # primary orbital elements
    __argument_of_perihelion = 0
    __mean_distance_from_sun = 1
    __eccentricity = 0
    __mean_anomaly = 0

    __ecentric_anomaly = 0


    # ====================================================================================================initialization
    def __init__(self, year, month, day, hour, minute):
        print ("calculating sun's position")

        # find the decimal hour
        self.__compute_decimal_hour(hour, minute)
        print("decimal hour: " + str(self.__decimal_hour))

        # find the decimal day
        self.__compute_decimal_day(year, month, day)
        print("decimal day: " + str(self.__decimal_day))

        #compute the oblicquity of the ecliptic
        self.__compute_obliquity_of_the_ecliptic()
        print("obliquity of the ecliptic: " + str(self.__obliquity_of_the_ecliptic))
        # compute the primary orbital elements
        self.__compute_primary_orbital_elements()
        print("argument of the perihelion: " + str(self.__argument_of_perihelion))
        print("eccentricity: " + str(self.__eccentricity))
        print("mean anomaly: " + str(self.__mean_anomaly))

        self.__compute_eccentric_anomaly()


    # =========================================================================================compute eccentric anomaly
    # computes the eccentric anomaly of the sun based off
    # of the mean anomaly and eccentricity
    def __compute_eccentric_anomaly(self):
        # first we need to convert the mean anomaly and
        # eccentricity to radians
        ma = math.radians(self.__mean_anomaly)
        e = math.radians(self.__eccentricity)

        # now we compute the eccentric anomaly
        ecentric_anomaly = ma
        ecentric_anomaly += e * math.sin(ma) * (1 + e * math.cos(ma))

        # set the variable
        self.__ecentric_anomaly = ecentric_anomaly


    # ==================================================================================compute primary orbital elements
    # this function takes the decimal day and uses it
    # to compute specific orbital elements for the sun
    def __compute_primary_orbital_elements(self):
        # 1st compute the argument of perihelion
        self.__argument_of_perihelion = 282.9404 + .00004709349 * self.__decimal_day

        # 2nd compute eccentricity
        self.__eccentricity = .016709 - .000000001151 * self.__decimal_day

        # 3rd compute the mean anomaly
        mean_anomaly = 356.0470 +  .9856002585 * self.__decimal_day

        # if the mean anomaly is > 360 we must subtract enough
        # from it until it is less than 360
        while mean_anomaly > 360:
            mean_anomaly = mean_anomaly - 360

        # else if the mean anomaly is negative, then add 360 until pos
        while mean_anomaly < 0:
            mean_anomaly = mean_anomaly + 360

        #now set the mean anomaly
        self.__mean_anomaly = mean_anomaly

        # the average mean from the sun is 1 since we are object is the sun
        # longitude of the ascending node for the sun is always 0
        # plan of earh's orbit is always 0 for the sun


    # =================================================================================compute obliquity of the ecliptic
    # finds the obliquity of the ecliptic
    def __compute_obliquity_of_the_ecliptic(self):
        self.__obliquity_of_the_ecliptic = 23.4393 - .0000003563 * self.__decimal_day


    # ===============================================================================================compute decimal day
    # this function takes in the year, month, and day
    # of the current date and computes the decimal
    # day. returns a float
    def __compute_decimal_day(self, year, month, day):

        # calculate the decimal day
        decimal_day = 367 * year - (7 * ((month + 9) / 12)) / 4
        decimal_day += 275 * month / 9
        decimal_day += day - 730530
        decimal_day += self.__decimal_hour / 24

        #set the decimal day
        self.__decimal_day = decimal_day


    # ==============================================================================================compute decimal hour
    # computes the fraction hour based on the time passed in
    def __compute_decimal_hour(self, hour, minute):
        # set the decimal hour
        self.__decimal_hour = hour + (minute / 60)






