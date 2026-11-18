"""Заявки технической поддержки (условный код)."""
from enum import Enum


class TicketStatus(Enum):
    NEW = "Новая"
    ASSIGNED = "Назначена"
    IN_PROGRESS = "В работе"
    DONE = "Выполнена"
    CLOSED = "Закрыта"


class Ticket:
    _next_number = 1

    def __init__(self, subscriber_id, description):
        self.number = Ticket._next_number
        Ticket._next_number += 1
        self.subscriber_id = subscriber_id
        self.description = description
        self.status = TicketStatus.NEW
        self.engineer = None

    def assign(self, engineer):
        self.engineer = engineer
        self.status = TicketStatus.ASSIGNED
