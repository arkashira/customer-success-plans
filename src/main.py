import json
from dataclasses import dataclass
from typing import List

@dataclass
class Customer:
    id: int
    name: str
    churn_score: float

class CustomerSuccessPlans:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def predict_churn(self, customer_id: int) -> float:
        for customer in self.customers:
            if customer.id == customer_id:
                return customer.churn_score
        return 0.0

    def generate_success_plan(self, customer_id: int) -> str:
        for customer in self.customers:
            if customer.id == customer_id:
                if customer.churn_score > 0.5:
                    return f"High risk customer {customer.name}, implement retention strategies"
                else:
                    return f"Low risk customer {customer.name}, continue with current strategies"
        return "Customer not found"

def load_dataset() -> List[Customer]:
    dataset = [
        Customer(1, "John Doe", 0.7),
        Customer(2, "Jane Doe", 0.3),
        Customer(3, "Bob Smith", 0.9),
    ]
    return dataset

def main():
    csp = CustomerSuccessPlans()
    dataset = load_dataset()
    for customer in dataset:
        csp.add_customer(customer)

    print(csp.predict_churn(1))
    print(csp.generate_success_plan(1))

if __name__ == "__main__":
    main()
