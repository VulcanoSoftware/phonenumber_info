import phonenumbers
from phonenumbers import geocoder
print("typ niet 04 maar typ +32")
number = input("geef het telefoon nummer waarvan u wilt achterhalen van welk land de landcode is example: +32 is voor belgie ... ")
#phone_number1 = phonenumbers.parse( a )
#print(geocoder.description_for_number(phone_number1, "be"))

ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))


input("")