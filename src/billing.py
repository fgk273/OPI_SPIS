"""Биллинг: тарифы, лицевой счёт, абонентская плата (условный код)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Tariff:
    name: str
    monthly_fee: float


class Account:
    def __init__(self, tariff, balance=0.0):
        self.tariff = tariff
        self.balance = balance
        self.blocked = False

    def top_up(self, amount):
        self.balance += amount
        if self.balance >= 0:
            self.blocked = False

    def charge_monthly_fee(self):
        self.balance -= self.tariff.monthly_fee
        if self.balance < 0:
            self.blocked = True
