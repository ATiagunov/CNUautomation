import re
import states_abbr
from geopy.geocoders import Nominatim
from datetime import date

geolocator = Nominatim(user_agent = "CNU")

#Initial
pick_loc = del_loc = ""
today = date.today()
miles = pieces = weight = 0
dims = "NO DIMENSIONS SPECIFIED"

def get_locations(txt_in):
    zip_code = "\s+\d{5}\s+"
    city_state = "\w+\,?\s\w{2}\,?"
    proper_addr = re.findall(city_state + zip_code, txt_in)
    global pick_loc, del_loc
    if (len(proper_addr) == 2):
        pick_loc = proper_addr[0].strip()
        del_loc = proper_addr[1].strip()
    else:
        zip_codes = re.findall(zip_code, txt_in)
        if (zip_codes):
            pickup_zip = zip_codes[0].strip()
            delivery_zip = zip_codes[1].strip()
            pick_loc = geolocator.geocode(query={'postalcode': pickup_zip, 'country' : 'US'})
            del_loc = geolocator.geocode(query={'postalcode': delivery_zip, 'country' : 'US'})


#Parse data
with open("test/a.txt", "r") as in_txt:
    read_content = in_txt.read()
    get_locations(read_content)
#   get_dates()
#   get_mileage()
#   get_pieces()
#   get_weight_dims
#   get_vehicle_type()

#get mileage
# pick_loc_coord = (pick_loc.latitude, pick_loc.longitude)
# del_loc_coord = (del_loc.latitude, del_loc.longitude)
# print(distance.distance(pick_loc_coord, del_loc_coord).miles)

#Fill the output file
if (len(pick_loc) and len(del_loc)):
    with open("test/output.txt", "w+") as out_txt:
        out_txt.write(f'Pick-up at: {pick_loc} \n')
        out_txt.write(f'Pick-up date (EST): {today} \n\n')
        out_txt.write(f'Deliver to: {del_loc} \n')
        out_txt.write(f'Delivery date (EST): {today} \n\n')
        out_txt.write(f'Miles: {miles} \n')
        out_txt.write(f'Pieces: {pieces} \n')
        out_txt.write(f'Weight: {weight} \n')
        out_txt.write(f'Dims: {dims} \n')
else:
    print("No zip codes provided")