from datetime import date
import re
import pgeocode

# Initial
source = "test/a.txt"

pick_loc = del_loc = ""
pick_date = del_date = date.today().strftime('%m/%d/%Y')
pick_time = del_time = '08:00 AM'
miles = pieces = weight = 1
dims = "NO DIMENSIONS SPECIFIED"


def get_location_from_zipcode(zipcode):

    full_location = ""
    data = pgeocode.Nominatim('US')
    retrieved = data.query_postal_code(zipcode)
    full_location = f'{retrieved.place_name}, {retrieved.state_code} {retrieved.postal_code}'
    return full_location


def get_locations(txt_in):
    zip_code = "\s+\d{5}\s+"
    state_codes = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    
    states = "(" + ")|(".join(state_codes) + ")"
    city_state = "\w+\,?\s" + states
    proper_addr = re.findall(city_state + zip_code, txt_in, re.IGNORECASE)
    global pick_loc, del_loc
    if (proper_addr != None and len(proper_addr) == 2):
        pick_loc = proper_addr[0].strip()
        del_loc = proper_addr[1].strip()
    else:
        zip_codes = re.findall(zip_code, txt_in)
        if (zip_codes != None and len(zip_codes) == 2):
            pick_loc = get_location_from_zipcode(zip_codes[0].strip())
            del_loc = get_location_from_zipcode(zip_codes[1].strip())

        else:
            city_states_raw = re.findall(city_state, txt_in)
            if (city_states_raw != None):
                city_state_only = "^[A-Za-z]+\,?\s[A-Z]{2}\,?$"
                res_list = []
                for str in city_states_raw:
                    print(str)
                    if re.match(city_state_only, str):
                        if (str[len(str)-1] == ','):
                            str = str[:len(str)-1]
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


def get_times(txt_in):
    time_mask = "(?:[0-1]?[0-9]|2[0-3]):[0-5][0-9]"
    found_times = re.findall(time_mask, txt_in)
    global pick_time, del_time
    if (found_times != None and len(found_times) == 2):
        pick_time = found_times[0]
        del_time = found_times[1]


def get_pieces(txt_in):
    pcs_before_at = "\d+\s+[@|crt]"
    line_with_pcs = re.search(pcs_before_at, txt_in, re.IGNORECASE)
    global pieces
    if (line_with_pcs != None):
        pieces = re.search("\d+", line_with_pcs[0])[0]


def get_dims(txt_in):
    dims_x = "\d+\.?\d?\s*[X|x]\s*\d+\.?\d?\s*[X|x]\s*\d+\.?\d?"
    line_with_dims = re.search(dims_x, txt_in)
    global dims
    if (line_with_dims != None):
        dims = line_with_dims[0]


def get_weight(txt_in):
    weight_lbs = "\d+(\.\d+)?\s*lbs?"
    weight_found = re.search(weight_lbs, txt_in, re.IGNORECASE)
    global weight
    if (weight_found):
        weight = weight_found[0]


def get_mileage(txt_in):
    miles_mask = "(?:([M|m]iles.*\d+)|(\d+\s*mi))"
    miles_found = re.search(miles_mask, txt_in)
    global miles
    if (miles_found != None):
        miles = miles_found[0]


def parse_data(source_txt):
    with open(source_txt, "r") as in_txt:
        read_content = in_txt.read()
        get_mileage(read_content)
        get_locations(read_content)
        get_dates(read_content)
        get_times(read_content)
        get_pieces(read_content)
        get_dims(read_content)
        get_weight(read_content)


# Fill the output file
def fill_output():
    if (len(pick_loc) and len(del_loc)):
        with open("test/output.txt", "w+") as out_txt:
            out_txt.write(f'Pick-up at: {pick_loc} \n')
            out_txt.write(f'Pick-up date (EST): {pick_date} {pick_time} \n\n')
            out_txt.write(f'Deliver to: {del_loc} \n')
            out_txt.write(f'Delivery date (EST): {del_date} {del_time} \n\n')
            out_txt.write(f'Miles: {miles} \n')
            out_txt.write(f'Pieces: {pieces} \n')
            out_txt.write(f'Weight: {weight} \n')
            out_txt.write(f'Dims: {dims} \n')
    else:
        print("Location wasn't found")


def transform(source="test/a.txt"):
    parse_data(source)
    fill_output()
