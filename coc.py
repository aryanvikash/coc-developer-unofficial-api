import requests
import json
import random
import string


class Coc:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def getmyip(self):
        url = 'https://api.ipify.org?format=json'
        response = requests.get(url)
        return response.json()['ip']

    def login(self):
        url = 'https://developer.clashofclans.com/api/login'
        headers = {
            'authority': 'developer.clashofclans.com',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'content-type': 'application/json',
            'sec-gpc': '1',
            'origin': 'https://developer.clashofclans.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://developer.clashofclans.com/',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'cookieconsent_status=dismiss'
        }
        data = {
            'email': self.email,
            'password': self.password
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.headers['set-cookie']

    def getAllkeys(self):
        cookie = self.login()
        url = 'https://developer.clashofclans.com/api/apikey/list'
        headers = {
            'authority': 'developer.clashofclans.com',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'content-type': 'application/json',
            'sec-gpc': '1',
            'origin': 'https://developer.clashofclans.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://developer.clashofclans.com/',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookie
        }

        response = requests.post(url, headers=headers, json={})
        return response.json()

    # print(loadlist())

    def createKey(self, ip=None):
        cookie = self.login()
        url = 'https://developer.clashofclans.com/api/apikey/create'
        headers = {
            'authority': 'developer.clashofclans.com',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'content-type': 'application/json',
            'sec-gpc': '1',
            'origin': 'https://developer.clashofclans.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://developer.clashofclans.com/',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookie
        }
        # random string
        randomdata = ''.join(
            [random.choice(string.ascii_letters + string.digits) for n in range(12)])
        data = {"name": randomdata, "description": randomdata,
                "cidrRanges": [ip if ip else self.getmyip()], "scopes": None}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()

    def deleteKey(self, id):
        cookie = self.login()
        url = 'https://developer.clashofclans.com/api/apikey/revoke'
        headers = {
            'authority': 'developer.clashofclans.com',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'content-type': 'application/json',
            'sec-gpc': '1',
            'origin': 'https://developer.clashofclans.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://developer.clashofclans.com/',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookie
        }
        data = {"id": id}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()


if __name__ == '__main__':
    c = Coc("yehebij705@wwdee.com", "vikash12")
    # print(c.createKey())
    # print(c.getAllkeys())
    print(c.getmyip())
