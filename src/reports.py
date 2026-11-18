"""Формирование отчётности (заготовка)."""


def monthly_summary(accounts):
    return {
        "accounts": len(accounts),
        "blocked": sum(1 for a in accounts if a.blocked),
        "total_balance": sum(a.balance for a in accounts),
    }
