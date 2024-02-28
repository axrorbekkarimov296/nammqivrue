import requests
import json
from datetime import datetime

BASE_URL = 'http://127.0.0.1:8000/api/myv'
response = requests.get("http://127.0.0.1:8000/api/myv/botusers")
data = response.json()


# Replace with your actual base URL


def createuser(username, name, user_id, phone):
    url = f"{BASE_URL}/botusers"

    # Assuming the response is in JSON format
    response = requests.get(url=url).json()

    user_exist = any(i['user_id'] == user_id for i in response)

    if not user_exist:
        # Sending JSON data using the json parameter
        requests.post(url=url, json={'username': username, 'name': name, 'user_id': user_id, 'phone': phone})
        return "Foydalanuvchi yaratildi"
    else:
        return "Foydalanuvchi mavjud"


def createariza(user_id,  name, kafedra, xona, body ):
    url = f"{BASE_URL}/arizaapi"
    tel = ' '
    response = requests.get("http://127.0.0.1:8000/api/myv/botusers")
    data = response.json()
    for i in data:
        if str(user_id) == i['user_id']:
            tel = i['phone']
            print(tel)
            break
        else:
            tel = ' '
    if body and user_id:
        dat = {
            "user_id": user_id,
            "name": name,
            "kafedra": kafedra,
            "xona": xona,
            "body": body,
            "tel": tel,

        }
        print(dat)
        try:
            response = requests.post(url=url, data=dat)
            response.raise_for_status()
            print(response.status_code)  # Serverdan gelen status kodi
            print(response.text)  # Serverdan gelen javob
            return "Ariza muvaffaqiyatli jo'natildi, javobni kuting"
        except requests.exceptions.RequestException as e:
            return f"Ariza jo'natilmadi. Xatolik: {e}"
    else:
            return "Amalyot bajarilmadi. Barcha maydonlarni to'ldiring."


def createkerio(user_id, fullname, department, rank, login, parol):
    url = f"{BASE_URL}/kerio"
    tel=' '
    response = requests.get("http://127.0.0.1:8000/api/myv/botusers")
    data = response.json()
    for i in data:
        if str(user_id) == i['user_id']:
            tel = i['phone']

            break
        else:
            tel = ' '
    if login and user_id:
        dat = {
            "user_id": user_id,
            "fullname": fullname,
            "department": department,
            "rank": rank,
            "login": login,
            "parol": parol,
            "tel": tel,
        }

        try:
            response = requests.post(url=url, data=dat)
            response.raise_for_status()
            print(response.status_code)  # Serverdan gelen status kodi
            print(response.text)  # Serverdan gelen javob
            return "Ariza muvaffaqiyatli jo'natildi, javobni kuting"
        except requests.exceptions.RequestException as e:
            return f"Ariza jo'natilmadi. Xatolik: {e}"
    else:
        return "Amalyot bajarilmadi. Barcha maydonlarni to'ldiring."


def createpochta(user_id, fullname, department, rank):
    url = f"{BASE_URL}/pochta"
    tel=' '
    response = requests.get("http://127.0.0.1:8000/api/myv/botusers")
    data = response.json()
    for i in data:
        if str(user_id) == i['user_id']:
            tel = i['phone']

            break
        else:
            tel = ' '
    if user_id:
        dat = {
            "user_id": user_id,
            "fullname": fullname,
            "department": department,
            "rank": rank,
            "tel": tel,
        }

        try:
            response = requests.post(url=url, data=dat)
            response.raise_for_status()
            print(response.status_code)  # Serverdan gelen status kodi
            print(response.text)  # Serverdan gelen javob
            return "Ariza muvaffaqiyatli jo'natildi, javobni kuting"
        except requests.exceptions.RequestException as e:
            return f"Ariza jo'natilmadi. Xatolik: {e}"
    else:
        return "Amalyot bajarilmadi. Barcha maydonlarni to'ldiring."
