from abc import ABC, abstractmethod


class AbstractStrategy(ABC):
    debug = False

    @staticmethod
    @abstractmethod
    def get_name():
        pass

    @staticmethod
    @abstractmethod
    def get_difficulty():
        pass

    @staticmethod
    @abstractmethod
    def apply(raatsel):
        pass
