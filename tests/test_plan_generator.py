import pytest
from customer_success_plans.plan_generator import generate_plan, _compute_churn_risk, CustomerMetrics


def test_churn_risk_basic():
    metrics = CustomerMetrics(days_since_last_login=30, support_tickets_open=0, usage_score=90)
    risk = _compute_churn_risk(metrics)
    assert risk == 0.0  # low risk


def test_churn_risk_high():
    metrics = CustomerMetrics(days_since_last_login=400, support_tickets_open=15, usage_score=20)
    risk = _compute_churn_risk(metrics)
    assert risk == 1.0  # cappe
