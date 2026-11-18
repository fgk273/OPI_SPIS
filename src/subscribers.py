"""Реестр абонентов и договоров (условный код)."""
from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Subscriber:
    full_name: str
    passport: str
    phone: str
    id: str = field(default_factory=lambda: str(uuid4()))


class SubscriberRegistry:
    """Хранит абонентов, не допускает дубликатов номера."""

    def __init__(self):
        self._items = {}
        self._phones = set()

    def register(self, subscriber):
        if subscriber.phone in self._phones:
            raise ValueError("Номер уже привязан к другому счёту")
        self._phones.add(subscriber.phone)
        self._items[subscriber.id] = subscriber
        return subscriber.id

    def get(self, subscriber_id):
        return self._items[subscriber_id]
