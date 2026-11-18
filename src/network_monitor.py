"""Мониторинг состояния сетевого оборудования (условный код)."""


def check_equipment(devices):
    """devices: словарь {имя: доступно?}. Возвращает список неисправных."""
    return [name for name, available in devices.items() if not available]
