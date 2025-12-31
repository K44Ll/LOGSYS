# Uso de ipinfo.io
import requests
import os
import subprocess
import sqlite3

def loc():
    ip = subprocess.check_output(['curl', 'https://ipinfo.io/ip']).decode('utf-8').strip()
    response = requests.get(f'https://ipinfo.io/{ip}/geo')
    data = response.json()
    city = data['city']
    loc = data['loc']
    country = data['country']
    tudo = [city, loc, country]
    return tudo

def checkloc():
    location = loc()
    city = location[0]
    loc_coords = location[1]
    country = location[2]
    conn = sqlite3.connect('dbs/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LOCATIONS WHERE CITY = ? AND LOC_COORDS = ? AND COUNTRY = ?", (city, loc_coords, country))
    result = cursor.fetchone()
    conn.close()
    if result == None:
        risco = 1
    else:
        risco = result[0]
    return risco

print(checkloc())