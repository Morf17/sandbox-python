import os
from configparser import RawConfigParser
from threading import Lock


class SettingsMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Settings(metaclass=SettingsMeta):

    def __init__(self):
        self.conf = RawConfigParser()
        root_dir = os.path.dirname(os.path.abspath(__file__))
        self.conf.read(os.path.join(root_dir, 'settings.ini'), encoding='utf-8')
        url_from_env = os.getenv('url', default=None)
        if url_from_env is not None:
            self.__url = url_from_env
        else:
            self.__url = self.conf.get('data', 'url')
        self.__login = self.conf.get('data', 'login')
        self.__password = self.conf.get('data', 'password')
        self.__driver_path = self.conf.get('data', 'driver_path')

    def get_url(self) -> str:
        return self.__url

    def get_login(self) -> str:
        return self.__login

    def get_password(self) -> str:
        return self.__password

    def get_driver_path(self) -> str:
        return self.__driver_path
