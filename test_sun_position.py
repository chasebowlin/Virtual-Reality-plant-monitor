from SunPosition import *

sun = SunPosition(2006, 'November', 15, 10, 35, '02°17\'23', '48°49\'00')

ephemeris = sun.get_position()

for item in ephemeris:
    print(str(item))
