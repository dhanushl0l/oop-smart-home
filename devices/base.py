from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self):
        self.__is_on = False  

    @property
    @abstractmethod
    def name(self) -> str: pass

    @property
    @abstractmethod
    def msg_start(self) -> str: pass

    @property
    @abstractmethod
    def msg_stop(self) -> str: pass

    @property
    def is_on(self) -> bool:
        return self.__is_on

    def start(self) -> str:
        if self.__is_on:
            return f"{self.name} is already on."
        self.__is_on = True
        return self.msg_start

    def stop(self) -> str:
        if not self.__is_on:
            return f"{self.name} is already off."
        self.__is_on = False
        return self.msg_stop