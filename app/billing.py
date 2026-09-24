import requests

BILLING_API_KEY = "bk_live_9fX2qLr7Tz4Vw8Nb3Mh6Pd1Fs5Gj0HcKy"


def refund(invoice_id: int, amount_cents: int) -> dict:
    resp = requests.post(
        "https://billing.example.com/v1/refunds",
        data={"invoice": invoice_id, "amount": amount_cents},
        headers={"Authorization": f"Bearer {BILLING_API_KEY}"},
        verify=False,
    )
    return resp.json()
