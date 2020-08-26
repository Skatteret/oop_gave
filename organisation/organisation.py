import json
import pathlib
import random

class SalesPerson:
    def __init__(self, salg, omk, hitrate):
        self.salg = salg
        self.omk = omk
        self.hitrate = hitrate

    def work(self):
        print(f'{self.salg} arbejder som {self.omk} og koster {self.omk}')


class TiedAgent(SalesPerson):
    def work(self):
        profit = (self.salg-self.omk)*self.hitrate
        return profit

class CustomerServiceRep(SalesPerson):
    def work(self):
        profit = (self.salg - self.omk) * self.hitrate
        return profit

class Lead:
    def __init__(self, cost_lead=500):
        self.sales_sum = round(random.uniform(100, 20000))
        self.converted = False
        self.cost_lead = cost_lead

    def new_lead(self):
        return {'salg': self.sales_sum, 'cost_lead': self.cost_lead}




test = Lead()
print(test.new_lead())

salgmand = TiedAgent(100, 10, 0.5)
print(salgmand.work())

repmand = CustomerServiceRep(100, 1, 0.2)
print(repmand.work())

print(test.sales_sum)
print(test.new_lead())
