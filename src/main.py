import re
import states_abbr
from geopy.geocoders import Nominatim
from datetime import date
from datetime import datetime

geolocator = Nominatim(user_agent = "CNU")

#Initial
source = "test/d.txt"
pick_loc = del_loc = ""
pick_date  = del_date = date.today().strftime('%m/%d/%Y')
miles = pieces = weight = 1
dims = "NO DIMENSIONS SPECIFIED"


def get_locations(txt_in):
    zip_code = "\s+\d{5}\s+"
    city_state = "\w+\,?\s\w{2}\,?"
    proper_addr = re.findall(city_state + zip_code, txt_in)
    global pick_loc, del_loc
    if (proper_addr != None and len(proper_addr) == 2):
        pick_loc = proper_addr[0].strip()
        del_loc = proper_addr[1].strip()
    else:
        zip_codes = re.findall(zip_code, txt_in)
        if (zip_codes != None and len(zip_codes) == 2):
            pickup_zip = zip_codes[0].strip()
            delivery_zip = zip_codes[1].strip()
            pick_loc = geolocator.geocode(query={'postalcode': pickup_zip, 'country' : 'US'})
            del_loc = geolocator.geocode(query={'postalcode': delivery_zip, 'country' : 'US'})
        else:
            city_states_raw = re.findall(city_state, txt_in)
            if (city_states_raw != None):
                city_state_only = "^\w+\,?\s[A-Z]{2}\,?$"
                res_list = []
                for str in city_states_raw:
                    if re.match(city_state_only, str):
                        res_list.append(str)
                if (len(res_list) == 2):        
                    pick_loc = res_list[0]
                    del_loc = res_list[1]
        

def get_dates(txt_in):
    multi_date = "\d+\s*(?:\/|-|\.)\s*\d+\s*(?:\/|-|\.)\s*\d+"
    proper_addr = re.findall(multi_date, txt_in)
    global pick_date, del_date
    if (proper_addr != None and len(proper_addr) == 2):
        pick_date = proper_addr[0].strip()
        del_date = proper_addr[1].strip()
        


def get_pieces(txt_in):
    pcs_before_at = "\d+\s+@"
    line_with_pcs = re.search(pcs_before_at, txt_in)
    global pieces
    if (line_with_pcs != None):
        pieces = re.search("\d+", line_with_pcs[0])[0]

def get_dims(txt_in):
    dims_x = "\d+\.?\d?\s*x\s*\d+\.?\d?\s*x\s*\d+\.?\d?"
    line_with_dims = re.search(dims_x, txt_in)
    global dims
    if (line_with_dims != None):
        dims = line_with_dims[0]

def get_weight(txt_in):
    weight_lbs = "\d+\s*lbs"
    weight_found = re.search(weight_lbs, txt_in)
    global weight
    if (weight_found != None):
        weight = weight_found[0]

def get_mileage(txt_in):
    miles_mask = "(?::((M|m)iles.*\d+)|(\d+\s*mi))"
    miles_found = re.search(miles_mask, txt_in)
    global miles
    if (miles_found != None):
        miles = miles_found[0]
    
                   
#Parse data
with open(source, "r") as in_txt:
    read_content = in_txt.read()
    get_locations(read_content)
    get_dates(read_content)
    get_pieces(read_content)
    get_dims(read_content)
    get_weight(read_content)
    get_mileage(read_content)

#get mileage
# pick_loc_coord = (pick_loc.latitude, pick_loc.longitude)
# del_loc_coord = (del_loc.latitude, del_loc.longitude)
# print(distance.distance(pick_loc_coord, del_loc_coord).miles)

#Fill the output file
if (len(pick_loc) and len(del_loc)):
    with open("test/output.txt", "w+") as out_txt:
        out_txt.write(f'Pick-up at: {pick_loc} \n')
        out_txt.write(f'Pick-up date (EST): {pick_date} \n\n')
        out_txt.write(f'Deliver to: {del_loc} \n')
        out_txt.write(f'Delivery date (EST): {del_date} \n\n')
        out_txt.write(f'Miles: {miles} \n')
        out_txt.write(f'Pieces: {pieces} \n')
        out_txt.write(f'Weight: {weight} \n')
        out_txt.write(f'Dims: {dims} \n')
else:
    print("No zip codes provided")