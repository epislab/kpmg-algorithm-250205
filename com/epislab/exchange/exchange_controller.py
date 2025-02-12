
from com.epislab.exchange.exchange_model import ExchangeModel
from com.epislab.exchange.exchange_service import ExchangeService


class ExchangeController:

    def __init__(self, **kwargs):
        self.amount = kwargs.get('amount')

    def get_result(self)->ExchangeModel:
        exchange = ExchangeModel()
        service = ExchangeService()
        exchange.amount = self.amount
        return service.execute(exchange)



        