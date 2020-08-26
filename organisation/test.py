class Organisation():
    tiedagent = 10
    costumerservicerep = 10
    leads = 1000

    def __init__(self, sales_people):
        self.sales_people = sales_people


    def work(self):
        for sales_person in self.sales_people:
            sales_person.work()


    def cost(self):
        total = 0
        for sales_person in self.sales_people:
            total = total + sales_person.cost
        return total


    @property
    def num_employees(self):
        return len(self.sales_people)

    @classmethod
    def from_json(cls, json_file):
        data = json.loads(pathlib.Path(json_file).read_text())
        return cls(sales_people=[
            SalesPerson(name=datum['name'],
                        agent_type=datum['agent_type'],
                        cost=datum['cost'])
            for datum in data])
