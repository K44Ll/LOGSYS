import socket
import sqlite3 as sql

def pegapc():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def check_dev():
    conn = sql.connect('dbs/data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DEVICES WHERE device_ip=?", (pegapc(),))
    N = cursor.fetchone()
    conn.close()
    if N == None:
        risco = 1
    else:
        risco = 0
    return risco