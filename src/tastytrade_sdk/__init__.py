from typing import Optional

from injector import Injector

from src.tastytrade_sdk.api import Api
from src.tastytrade_sdk.instruments import Instruments
from src.tastytrade_sdk.market_metrics import MarketMetrics
from src.tastytrade_sdk.watchlists import Watchlists


class Tastytrade:
    def __init__(self, login: Optional[str] = None, password: Optional[str] = None):
        self.__injector = Injector()
        if login and password:
            self.login(login, password)

    def login(self, login: str, password: str):
        self.__injector.get(Api).login(login, password)

    @property
    def instruments(self) -> Instruments:
        return self.__injector.get(Instruments)

    @property
    def market_metrics(self) -> MarketMetrics:
        return self.__injector.get(MarketMetrics)

    @property
    def watchlists(self) -> Watchlists:
        return self.__injector.get(Watchlists)


__all__ = ['Tastytrade']