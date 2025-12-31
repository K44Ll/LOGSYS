import subprocess
import sqlite3 as sql

def ip():
    ip = subprocess.check_output(['curl', 'checkip.amazonaws.com']).decode('utf-8').strip()
    return ip
def checkip(ip):
    conn = sql.connect('dbs/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT IP_ADDRESS FROM ALLOWED_IPS WHERE IP_ADDRESS = ?", (ip,))
    locate = cursor.fetchone()
    conn.close()
    if locate == None:
        risco = 1
    else:
        risco = 0
    return risco