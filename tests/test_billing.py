import unittest

from src.billing import Account, Tariff
from src.subscribers import Subscriber, SubscriberRegistry


class BillingTest(unittest.TestCase):
    def test_block_on_negative_balance(self):
        acc = Account(Tariff("Базовый", 300), balance=100)
        acc.charge_monthly_fee()
        self.assertTrue(acc.blocked)
        acc.top_up(500)
        self.assertFalse(acc.blocked)

    def test_phone_is_unique(self):
        reg = SubscriberRegistry()
        reg.register(Subscriber("Иванов И.И.", "0000 000000", "+70000000001"))
        with self.assertRaises(ValueError):
            reg.register(Subscriber("Петров П.П.", "1111 111111", "+70000000001"))


if __name__ == "__main__":
    unittest.main()
