from main import Customer, CustomerSuccessPlans, load_dataset

def test_customer_success_plans():
    csp = CustomerSuccessPlans()
    dataset = load_dataset()
    for customer in dataset:
        csp.add_customer(customer)

    assert csp.predict_churn(1) == 0.7
    assert csp.generate_success_plan(1) == "High risk customer John Doe, implement retention strategies"

def test_customer_not_found():
    csp = CustomerSuccessPlans()
    assert csp.predict_churn(4) == 0.0
    assert csp.generate_success_plan(4) == "Customer not found"

def test_load_dataset():
    dataset = load_dataset()
    assert len(dataset) == 3
    assert dataset[0].id == 1
    assert dataset[0].name == "John Doe"
    assert dataset[0].churn_score == 0.7
