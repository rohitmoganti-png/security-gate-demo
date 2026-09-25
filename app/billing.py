import os
from datetime import datetime, timezone

import requests
from dateutil.relativedelta import relativedelta


def _api_key() -> str:
    return os.environ["BILLING_API_KEY"]  # from the environment, never in code


def refund(invoice_id: int, amount_cents: int) -> dict:
    resp = requests.post(
        "https://billing.example.com/v1/refunds",
        data={"invoice": invoice_id, "amount": amount_cents},
        headers={"Authorization": f"Bearer {_api_key()}"},
        timeout=10,  # TLS verification stays ON (the default)
    )
    resp.raise_for_status()
    return resp.json()


def refund_deadline(issued_at: datetime) -> datetime:
    """Refunds are allowed for one month after the invoice was issued."""
    return issued_at.astimezone(timezone.utc) + relativedelta(months=1)
