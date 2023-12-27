import urllib3

# MapBox Methonds
token = "pk.eyJ1IjoiYWxla3MzMTciLCJhIjoiY2xxbXVhbGdpMGJhMDJqbXdkaGlmdTJ3eiJ9.ieO4fwnIp1nXKPGjOmrC8A"

# Getting mileage using directions module
# input strings of pattern: longitude,latitude
# returns distance between given points in miles
def get_mileage(origin, destination):
    directions = urllib3.request("GET", f"https://api.mapbox.com/directions/v5/mapbox/driving-traffic/{origin};{destination}?exclude=ferry&access_token={token}").json()
    distance_meters = directions['routes'][0]['distance']
    distance_miles = distance_meters // 1609.344
    return distance_miles


# Getting compete address, longitude and latitude from incomplete address
# returns list of 2 strings: address, long_lat
def get_geocode(location):
    geocoding = urllib3.request("GET", f"https://api.mapbox.com/geocoding/v5/mapbox.places/{location}.json?access_token={token}").json()
    addr = geocoding['features'][0]['place_name']
    longitude = str(geocoding['features'][0]['center'][0])
    latitude = str(geocoding['features'][0]['center'][1])
    addr = addr.rsplit(',', 1)[0]
    return [addr, longitude + ',' + latitude]