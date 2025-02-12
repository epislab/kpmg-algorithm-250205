
from com.epislab.exchange.exchange_model import ExchangeModel


class ExchangeService:

    def __init__(self):
        pass


    def get_unit_count(self, amount, won_list):
        money = amount
        won_dict = {}
        for won in won_list:
            won_dict[won] = money // won
            money %= won
        return won_dict

    def execute(self, exchange: ExchangeModel) -> ExchangeModel:
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
        
        
        won_dict = self.get_unit_count(exchange.amount, won_list)
        print("-------💰거스름돈💰-------")
        for won, count in won_dict.items():
            print(f"{won}원: {count}개")
        print("-------끝-------")

        temp = ''
        for won, count in won_dict.items():
            temp += f"{won}원: {count}개<br/>"

        exchange.result = temp
        return exchange