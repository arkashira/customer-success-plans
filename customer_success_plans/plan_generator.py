"""
Generate a simple AI‑powered customer‑success plan.

The plan is a short text that includes:
* a churn risk score (0‑1)
* a brief recommendation list

The churn risk is computed from a handful of customer metrics:
    - days_since_last_login
    - support_tickets_open
    - usage_score (0‑100)

The function is intentionally lightweight so it can be used in unit tests
and as a building block for larger pipelines.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class CustomerMetrics:
    days_since_last_login: int
    support_tickets_open: int
    usage_score: int  # 0‑100


def _compute_churn_risk(metrics: CustomerMetrics) -> float:
    """
    Very naive churn‑risk estimator.

    * More days since last login → higher risk
    * More open tickets → higher risk
    * Lower usage score → higher risk

    Returns a float between 0 (no risk) and 1 (certain churn).
    """
    risk = 0.0
    risk += min(metrics.days_since_last_login / 365, 1.0) * 0.4
    risk += min(metrics.support_tickets_open / 10, 1.0) * 0.3
    risk += (1 - metrics.usage_score / 100) * 0.3
    return round(min(max(risk, 0.0), 1.0), 3)


def generate_plan(customer_id: str, raw_metrics: Dict[str, int]) -> str:
    """
    Generate a short success plan for a customer.

    Parameters
    ----------
    customer_id : str
        Unique identifier for the customer.
    raw_metrics : dict
        Dictionary with keys:
            - days_since_last_login
            - support_tickets_open
            - usage_score

    Returns
    -------
    str
        A formatted plan string.
    """
    metrics = CustomerMetrics(**raw_metrics)
    risk = _compute_churn_risk(metrics)

    plan_lines: List[str] = [
        f"Customer ID: {customer_id}",
        f"Churn Risk: {risk:.0%}",
        "",
        "Recommended actions:",
    ]

    if risk > 0.6:
        plan_lines.append("- Prioritize a proactive outreach call.")
    if metrics.support_tickets_open > 0:
        plan_lines.append("- Resolve open tickets within 48 h.")
    if metrics.usage_score < 50:
        plan_lines.append("- Offer a usage‑boost workshop.")
    if risk < 0.3:
        plan_lines.append("- Continue monitoring; maintain engagement.")

    return "\n".join(plan_lines)