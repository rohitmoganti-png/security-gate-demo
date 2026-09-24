from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: str
    is_admin: bool = False


@dataclass
class Invoice:
    id: int
    owner_id: int
    amount_cents: int
    status: str
