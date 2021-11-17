# install phonenumbers on cmd prompt by typing "pip install phonenumbers"

import phonenumsber

from phonenumbers import timezone,geocoder,carrier

number =input("Enter Your Number with +__ :  ")
phone =phonenumbers.parse(number)
time =timezone.time_zones_for_number(phone)
carrier =carrier.name_for_number(phone, "en")
reg =geocoder.description_for_number(phone, "en")


print(phone)
print(time)
print(carrier)
print(reg)