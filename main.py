import sqlite3 as sql
import bcrypt

from libs.check_ip import ip 
from libs.check_loc import loc 
from libs.check_dev import pegapc 
from libs.retorna_risco import Retorno, retorna_risco
from libs.check_hora import checahora


def HOME():
    print('''
██╗░░░░░░█████╗░░██████╗░░██████╗██╗░░░██╗░██████╗
██║░░░░░██╔══██╗██╔════╝░██╔════╝╚██╗░██╔╝██╔════╝
██║░░░░░██║░░██║██║░░██╗░╚█████╗░░╚████╔╝░╚█████╗░
██║░░░░░██║░░██║██║░░╚██╗░╚═══██╗░░╚██╔╝░░░╚═══██╗
███████╗╚█████╔╝╚██████╔╝██████╔╝░░░██║░░░██████╔╝
╚══════╝░╚════╝░░╚═════╝░╚═════╝░░░░╚═╝░░░╚═════╝░
''')
    print("[01] Log-in")
    print("[02] Registro")
    print("[00] Sair")

    op = input(">_ ")

    if op == "01":
        LOGIN()
    elif op == "02":
        REGISTRO()
    elif op == "00":
        exit()
    else:
        print("Opção inválida!")


def LOGIN():
    print("\n=== LOGIN ===")
    username = input("Usuário >_ ")
    senha = input("Senha >_ ").encode()

    try:
        with sql.connect("dbs/data.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT PASSWORD_HASH FROM USERS WHERE USERNAME = ?",
                (username,)
            )
            result = cursor.fetchone()

        if result and bcrypt.checkpw(senha, result[0]):
            print("Senha correta ✅")

            retorna_risco()  # inicializa RH, RI, RL, RD
            risco = Retorno()

            print(f"Risco calculado: {risco:.3f}")
            if risco < 0.75:
                print("Acesso concedido ✅")
            else:
                print("Acesso negado ❌")
            HOME()
        else:
            print("Usuário ou senha incorretos ❌")

    except Exception as e:
        print("Erro no login:", e)

    HOME()


def REGISTRO():
    print("\n=== REGISTRO ===")
    username = input("Usuário >_ ")
    senha_raw = input("Senha >_ ")

    senha_hash = bcrypt.hashpw(senha_raw.encode(), bcrypt.gensalt())

    device = pegapc()
    loc_data = loc()
    ip_addr = ip()

    city = loc_data[0]
    loc_coords = loc_data[1]
    country = loc_data[2]

    try:
        with sql.connect("dbs/data.db") as conn:
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO USERS (USERNAME, PASSWORD_HASH) VALUES (?, ?)",
                (username, senha_hash)
            )

            cursor.execute(
                "INSERT INTO DEVICES (device_ip) VALUES (?)",
                (device,)
            )

            cursor.execute(
                "INSERT INTO LOCATIONS (CITY, LOC_COORDS, COUNTRY) VALUES (?, ?, ?)",
                (city, loc_coords, country)
            )

            cursor.execute(
                "INSERT INTO ALLOWED_IPS (IP_ADDRESS) VALUES (?)",
                (ip_addr,)
            )

            conn.commit()

        print("Registro concluído com sucesso ✅")

    except Exception as e:
        print("Erro ao registrar:", e)

    HOME()


HOME()
