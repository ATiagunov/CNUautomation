from datetime import date, timedelta
import re, MapBox

origin_geocode = destination_geocode = []
pick_date = date.today().strftime('%m/%d/%Y')
del_date = (date.today() + timedelta(days=1)).strftime('%m/%d/%Y')
pick_time = del_time = '08:00 AM'
miles = pieces = weight = 1
dims = "NO DIMENSIONS SPECIFIED"


def get_geocode(txt_in):
    global origin_geocode, destination_geocode
    best_query = []
    zip_code = "\s+\(?\d{5}\)?\,?\s+"
    zip_codes = re.findall(zip_code, txt_in)
    #if zip codes found - best query
    if (zip_codes != None and len(zip_codes) == 2):
        best_query = zip_codes
    
    #otherwise checking city and state info
    else:
        city_state = "(?:[A-Z][a-z]+\s)*[A-Z][a-z]+\,?\s(?i:AK|AL|AR|AZ|CA|CO|CT|DC|DE|FL|GA|HI|IA|ID|IL|IN|KS|KY|LA|MA|MD|ME|MI|MN|MO|MS|MT|NC|ND|NE|NH|NJ|NM|NV|NY|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VA|VT|WA|WI|WV|WY)(?:\s|\,)"
        city_states = re.findall(city_state, txt_in)
        if (city_states != None):
            if (len(city_states) == 2):
                best_query = city_states
            #need better solution
            elif(len(city_states) > 2):
                origin_geocode = MapBox.get_geocode(city_states[1])
                destination_geocode = MapBox.get_geocode(city_states[2])

                
    if(best_query):
        origin_geocode = MapBox.get_geocode(best_query[0])
        destination_geocode = MapBox.get_geocode(best_query[1])


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
    global miles
    if (origin_geocode and destination_geocode):
        miles = f'{MapBox.get_mileage(origin_geocode[1], destination_geocode[1]):g}'



def parse_data(read_content):
        get_geocode(read_content)
        if (origin_geocode and destination_geocode):
            get_mileage(read_content)
            get_dates(read_content)
            get_times(read_content)
            get_pieces(read_content)
            get_dims(read_content)
            get_weight(read_content)


# Fill the output file
def fill_output():
    if (origin_geocode and destination_geocode):
        result = f"""Pick-up at: {origin_geocode[0]}
Pick-up date (EST): {pick_date} {pick_time}
Deliver to: {destination_geocode[0]}
Delivery date (EST): {del_date} {del_time}

Miles: {miles}
Pieces: {pieces}
Weight: {weight}
Dims: {dims}
        """
        return result
    else:
        return "Location wasn't found"


def transform(source):
#    if (len(source) > 0):
    parse_data(source)
    return fill_output()
