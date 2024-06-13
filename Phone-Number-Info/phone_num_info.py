
import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier

PhoneNumber = input("Enter Phone Number: ")
number = phonenumbers.parse(PhoneNumber)

country = ("Country: " + geocoder.description_for_number(number, "en"))
sp = ("Service Provider: " + carrier.name_for_number(number, "en"))

print(country)
print(sp)
