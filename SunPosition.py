import os
import math

# this class takes in the date and time of the current time
# and calculates the position of the sun in the sky
from decimal import Decimal



class SunPosition:
    # a dictionary that holds the data for holding how many
    # days since the begging of a year the 1st of the month is
    # DOES NOT HOLD DATA FOR LEAP YEAR
    __days_since_year_start = {'February': 32,
                               'March': 60,
                               'April': 91,
                               'May': 121,
                               'June': 152,
                               'July': 182,
                               'August': 213,
                               'September': 244,
                               'October': 274,
                               'November': 305,
                               'December': 335}

    # will hold the two values that will need to be returned in order
    # to find the ephemeris of the sun
    __sun_elevation_angle = 0.00
    __sun__azimuth_angle = 0.00


    # ====================================================================================================initialization
    def __init__(self, year, month, day, hour, minute, longitude, latitude):
        # convert the longitutde and latitude to degrees
        longitude = self.__convert_tude(longitude)
        latitude = self.__convert_tude(latitude)

        print ("longitude: " + str(longitude) + "   latitude: " + str(latitude))

        fractional_hour = self.__find_fractional_hour(hour, minute)
        print("Fractional hour: " + str(fractional_hour))

        fractional_year = self.__find_fractional_year(month, day, hour, minute)
        print("Fractional year: " + str(fractional_year))

        declination = self.__find_declination_of_the_sun(fractional_year)
        print("Declination: " + str(declination))

        correction = self.__find_time_correction_for_solar_angle(fractional_year)
        print("Correction: " + str(correction))

        sha = self.__find_solar_hour_angle(fractional_hour, correction, longitude)
        print("Solar hour angle: " + str(sha))

        sza = self.__find_sun_zenith_angle(declination, sha, latitude)
        print("Solar zenith angle: " + str(sza))

        self.__sun_elevation_angle = self.__find_sun_elevation_angle(sza)
        print("Sun elevation angle: " + str(self.__sun_elevation_angle))

        self.__sun__azimuth_angle = self.__find_sun_azimuth_angle(declination, latitude, sza)
        print("Sun azimuth angle: " + str(self.__sun__azimuth_angle))


    # =====================================================================================================get ephemeris
    # a simple function that returns a touple of the sun elevation
    # angle and the sun azimuth angle
    def get_ephemeris(self):
        return (self.__sun__azimuth_angle, self.__sun_elevation_angle)



    # =================================================================================================sun azimuth angle
    # finds the sun azimuth angle based on the declination, latitude, and
    # the solar zenith angle
    def __find_sun_azimuth_angle(self, declination, latitude, sza):
        # first, convert the parameters into radians
        declination = math.radians(declination)
        latitude = math.radians(latitude)
        sza = math.radians(sza)

        # now plug in the parameters and calculate the sun azimuth angle
        saa = (math.sin(declination) - math.sin(latitude) * math.cos(sza)) / (math.cos(latitude) * math.sin(sza))
        saa = math.acos(saa)

        # convert the sun azimuth angle to degrees
        saa = math.degrees(saa)

        # round the solar azimuth angle to the 5th decimal and return it
        return round(saa, 5)


    # ===============================================================================================sun elevation angle
    # finds the sun elevation angle based off of the sun zenith angle
    def __find_sun_elevation_angle(self, sza):
        # first, convert the sza to radians
        sza = math.radians(sza)

        # IF cos(sun zenith angle) is greater than 1, then just use 1
        if math.cos(sza) > 1:
            sza = 1
        # ELSE IF cos(sun zenith angle) less than -1, just use -1
        elif math.cos(sza) < -1:
            sza = -1

        # convert the sza back to degrees
        sza = math.degrees(sza)

        # calculate the sun elevation angle, round it off
        # to the 3rd decimal, and return it
        return round(90 - sza, 3)


    # ================================================================================================solar zenith angle
    # finds the sun zenith angle based off of the latitude passed in, declination,
    # and the solar hour angle
    def __find_sun_zenith_angle(self, declination, sha, latitude):
        # first convert all the parameters to radians
        declination = math.radians(declination)
        sha = math.radians(sha)
        latitude = math.radians(latitude)

        # now plug in the parameters and calculate the sun zenith angle
        sza = math.sin(latitude) * math.sin(declination)
        sza += math.cos(latitude) * math.cos(declination) * math.cos(sha)

        # convert the solar zenith angle so far to radians and
        # plug it into the last part of the equation
        sza = math.acos(sza)

        # convert the solar zenith angle back to angles
        sza = math.degrees(sza)

        # round the solar zenith angle to the 5th decimal and return
        return round(sza, 5)


    # ==================================================================================================solar hour angle
    # finds the solar hour angle based off of the fractional hour, the time correction
    # for solar angle, and the longitude passed in by the user
    def __find_solar_hour_angle(self, fractional_hour, correction, longitude):

        # compute the solar hour angle based off of the fractional hour,
        # solar angle correction, and the longitude.
        sha = (fractional_hour - 12) * 15
        sha += longitude
        sha += correction

        # round off the answer to the 4th decimal place
        sha = round(sha, 4)

        # IF the solar hour angle is more than 180, we must add (-360)
        if sha > 180:
            sha += (-360)

        # ELSE IF the solar hour angle is less than -180, we must add 360
        elif sha < -180:
            sha += 360

        # return the solar hour angle
        return sha


    # ========================================================================================correction for solar angle
    # finds the correction for the solar angle based off of the fractional year
    def __find_time_correction_for_solar_angle(self, fractional_year):
        # first, convert the fractional year to radians
        fractional_year = math.radians(fractional_year)

        # plug the fractional year into the equation
        correction = .004297
        correction += .107029 * math.cos(fractional_year)
        correction += (-1.837877) * math.sin(fractional_year)
        correction += (-.837378) * math.cos(2 * fractional_year)
        correction += (-2.340475) * math.sin(2 * fractional_year)

        # round off the correction to the 5th decimal place and return
        return round(correction, 5)


    # ============================================================================================declination of the sun
    # finds the declination of the sun based of a specific equation that
    # takes in a fractional_year
    def __find_declination_of_the_sun(self, fractional_year):
        # convert the fractional year into radians
        fractional_year = math.radians(fractional_year)

        # calculate the declination of the sun
        declination = .396372
        declination += (-22.91327) * math.cos(fractional_year)
        declination += 4.02543 * math.sin(fractional_year)
        declination += (-.387205) * math.cos(2 * fractional_year)
        declination += .051967  * math.sin(2 * fractional_year)
        declination += (-.154527) * math.cos(3 * fractional_year)
        declination += .084798 * math.sin(3 * fractional_year)

        # round off the declination to the 4th decimal place and return
        return round(declination, 4)


    # ===================================================================================================fractional year
    # finds the fractional year based off of the total number of days since
    # the beginning of the year and the fractional hour
    def __find_fractional_year(self, month, day, hour, minute):
        # holds the total number of days from the beginning of the
        # year to the passed in date
        total_days = 0

        '''
        go through the dictionary and find which month was passed in
        and grab the number of days since the beginning of the year.
        
        the value we grab represents the 1st of the month (Feb 1st = 32)
        
        break out once we have found the one we are looking for 
        '''
        for m, days in self.__days_since_year_start.items():
            if m == month:
                total_days = days
                break

        # now add on the day of the month -1 because we have already
        # taken in account
        total_days += day - 1

        # now we need to find the fractional hour
        fractional_hour = self.__find_fractional_hour(hour, minute)

        # now plug in all the predetermined information that we found
        # into the equation
        fractional_year = Decimal((360 / 365.25) * (total_days + (fractional_hour / 24)))

        # round off the fractional year to the 3rd decimal place and return
        return round(fractional_year, 3)


    # ===================================================================================================fractional hour
    # a simple equation that returns the fractional hour
    def __find_fractional_hour(selfself, hour, minute):
        return hour + (minute / 60)

    # ======================================================================================================convert tude
    # takes in a longitude or latitude and either converts into degrees or
    # degrees minutes seconds format (aka 00° 00' 00")
    def __convert_tude(self, tude):
        # check if it is in degrees minutes seconds format
        if "°" in tude and '\'' in tude:
            #split the string up into degrees, minutes, and seconds
            split1 = tude.split('°')
            if '\'' in split1[1]:
                split2 = split1[1].split('\'')

            # convert the tude to degrees and return
            tude = float(split1[0])
            tude += float(split2[0]) / 60
            tude += float(split2[1]) / 3600
            return tude
