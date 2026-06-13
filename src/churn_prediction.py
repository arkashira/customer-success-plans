import json
from dataclasses import dataclass
from typing import List

@dataclass
class Customer:
    id: int
    usage_data: List[float]

class ChurnPredictionModel:
    def __init__(self):
        self.model = {}

    def train(self, customers: List[Customer]):
        for customer in customers:
            self.model[customer.id] = sum(customer.usage_data) / len(customer.usage_data)

    def predict(self, customer_id: int) -> float:
        if customer_id in self.model:
            return self.model[customer_id]
        else:
            return 0.0

class ChurnPredictionAPI:
    def __init__(self):
        self.model = ChurnPredictionModel()

    def train(self, customers: List[Customer]):
        self.model.train(customers)

    def predict(self, customer_id: int) -> float:
        return self.model.predict(customer_id)

    def get_prediction(self, customer_id: int) -> dict:
        prediction = self.predict(customer_id)
        return {"customer_id": customer_id, "prediction": prediction}
