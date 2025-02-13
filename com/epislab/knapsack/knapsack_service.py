
from com.epislab.knapsack.item_model import ItemModel
from com.epislab.knapsack.knapsack_model import KnapsackModel


class KnapsackService:

    def __init__(self):
        pass


    def execute(self,knapsack) -> KnapsackModel:
        max_capacity = knapsack.max_capacity
        profit1 = knapsack.profit1
        weight1 = knapsack.weight1
        profit2 = knapsack.profit2
        weight2 = knapsack.weight2
        profit3 = knapsack.profit3
        weight3 = knapsack.weight3
        profit4 = knapsack.profit4
        weight4 = knapsack.weight4
        profit_list = [profit1, profit2, profit3, profit4]
        weight_list = [weight1, weight2, weight3, weight4]
        temp =[]
        # profit_per_weight = [profit_list[i] / weight_list[i] for i in range(4)]
        for i in range(4):
            temp.append(profit_list[i] / weight_list[i])

        temp = [4, 2, 3, 5]
        profit_per_weight = [temp[0], temp[1], temp[2], temp[3]]

        itm1 = ItemModel()
        itm1.name = "item1"
        itm1.profit = profit1
        itm1.weight = weight1
        itm1.profit_per_weight = profit_per_weight[0]

        item1 = {"name":"item1", "profit":profit1, "weight":weight1, "profit_per_weight":profit_per_weight[0]}
        item2 = {"name":"item2", "profit":profit2, "weight":weight2, "profit_per_weight":profit_per_weight[1]}
        item3 = {"name":"item3", "profit":profit3, "weight":weight3, "profit_per_weight":profit_per_weight[2]}
        item4 = {"name":"item4", "profit":profit4, "weight":weight4, "profit_per_weight":profit_per_weight[3]}

        items = [item1, item2, item3, item4] 


        for i in range(4):
            for j in range(i+1, 4):
                if items[i].get("profit_per_weight") > items[j].get("profit_per_weight"):
                    items[i], items[j] = items[j], items[i]
  
        for i in items:
            print("🔥🦉",i.get("name"))

        total_weight = max_capacity # 10
        total_profit = 0

        for i in range(4):
            if items[i].get("weight") <= total_weight:
                total_weight -= items[i].get("weight")
                total_profit += items[i].get("profit")
            else:
                # 3/4 인 경우 처리 
                break
        
        result = self.knapsack(max_capacity, profit1, weight1, profit2, weight2, profit3, weight3, profit4, weight4)
        knapsack.result = result
        return knapsack
