import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadProperties:
    @staticmethod
    def get_user():
        user = config.get('login info', 'username')
        return user

    @staticmethod
    def get_password():
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def get_url():
        url = config.get('login info', 'baseurl')
        return url


