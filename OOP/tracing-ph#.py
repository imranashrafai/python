print("======================== Tracing Location ========================")
import phonenumbers
from phonenumbers import geocoder
ph1=phonenumbers.parse("+923061439430")
print("Phone Number's Locations")
print(geocoder.description_for_valid_number(ph1,"en"))
