from dataclasses import dataclass
@dataclass
class ItemModel:
    name: str
    profit : int
    weight: int
    profit_per_weight: int


    @property
    def name(self) -> int:
        return self._name
    @name.setter
    def name(self, name):
        self._name = name


    @property
    def profit(self) -> int:
        return self._profit
    @profit.setter
    def profit(self, profit):
        self._profit = profit

    @property
    def weight(self) -> int:
        return self._weight
    @weight.setter
    def weight(self, weight):
        self._weight = weight


    @property
    def profit_per_weight(self) -> int:
        return self._profit_per_weight
    @profit_per_weight.setter
    def profit_per_weight(self, profit_per_weight):
        self._profit_per_weight = profit_per_weight
