from churn_prediction import ChurnPredictionAPI, Customer
import pytest

def test_train_and_predict():
    api = ChurnPredictionAPI()
    customers = [Customer(1, [10.0, 20.0, 30.0]), Customer(2, [5.0, 10.0, 15.0])]
    api.train(customers)
    assert api.predict(1) == 20.0
    assert api.predict(2) == 10.0

def test_predict_unknown_customer():
    api = ChurnPredictionAPI()
    customers = [Customer(1, [10.0, 20.0, 30.0])]
    api.train(customers)
    assert api.predict(2) == 0.0

def test_get_prediction():
    api = ChurnPredictionAPI()
    customers = [Customer(1, [10.0, 20.0, 30.0])]
    api.train(customers)
    prediction = api.get_prediction(1)
    assert prediction["customer_id"] == 1
    assert prediction["prediction"] == 20.0
