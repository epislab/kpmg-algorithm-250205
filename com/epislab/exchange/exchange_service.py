
from com.epislab.exchange.exchange_model import ExchangeModel


class ExchangeService:

    def __init__(self):
        pass

    def execute(self, exchange: ExchangeModel) -> ExchangeModel:
        won_list = self.get_won_list()
        currency_list = won_list
        currency_dict = self.get_currency_counts(exchange.amount, currency_list)
        self.print_currency_dict(currency_dict)
        exchange.result = self.format_currency_counts(currency_dict, currency_unit='원')
        return exchange

    def get_currency_dict(self, amount, currency_list)->dict:
        money = amount
        currency_dict = {}
        for currency in currency_list:
            currency_dict[currency] = money // currency
            money %= currency
        return currency_dict

    def get_won_list(self):
        WON_50000 = 50000
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10
        won_list = [WON_50000, WON_10000, WON_5000,
                        WON_1000, WON_500, WON_100, WON_50, WON_10]
        return won_list

    def format_currency_counts(self, currency_dict, currency_unit):
        temp = ''
        for currency, count in currency_dict.items():
            temp += f"{currency}{currency_unit}: {count}개<br/>"
        return temp

    def print_currency_dict(self, currency_dict):
        print("-------💰거스름돈💰-------")
        for won, count in currency_dict.items():
            print(f"{won}원: {count}개")
        print("-------끝-------")