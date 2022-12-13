import json
import requests
import sqlite3 as sql

def ip_to_loc():

    api_key = "AIzaSyCxUJvUYcT-DO2xIbsatBmp6gEW2WAE9eY"

    LOCATION_API_KEY = api_key

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={LOCATION_API_KEY}'
    data = {
        'considerIp': True,
    }

    result = requests.post(url, data)

    loc = json.loads(result.text)
    loc = loc["location"]

    lat = f"{loc['lat']:.03f}"      # 위도
    lng = f"{loc['lng']:.03f}"      # 경도

    return lat, lng

def loc_to_xy(lat, lng):

    con = sql.connect("DB\Location.db")
    cmd = con.cursor()

    query = f"SELECT ONE, TWO, THR, X, Y FROM weatherDB WHERE LAT = '{lat}' AND LNG = '{lng}'"
    cmd.execute(query)
    
    data = cmd.fetchall()

    # location = data[0][0], data[0][1], data[0][2]
    # x, y = data[0][3], data[0][4]

    print(data)


lat, lng = ip_to_loc()
loc_to_xy(lat, lng)