import requests


class Form:
    def __init__(self, login:str, password:str, mail=None, url=None):
        self.login = login
        self.password = password
        self.mail = mail
        self.url = url

    def set_web_url(self, url):
        try:
            response = requests.head(url, timeout=5, allow_redirects=True)
            self.url = url
        except requests.RequestException as error:
            print(f"Error occurred: {error}")

