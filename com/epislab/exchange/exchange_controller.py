
from com.epislab.exchange.exchange_model import ExchangeModel
from com.epislab.exchange.exchange_service import ExchangeService


class ExchangeController:

    def __init__(self, **kwargs):
        self.amount = kwargs.get('amount')
        self.currency = kwargs.get('currency')

    def get_result(self)->ExchangeModel:
        exchange = ExchangeModel()
        service = ExchangeService()
        exchange.amount = self.amount
        exchange.currency = self.currency
        return service.execute(exchange)



        