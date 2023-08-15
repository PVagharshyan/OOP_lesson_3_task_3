class obj:
    _count = 1

    def __init__(self) -> None:
        self._serial_number = self._count
        obj._count += 1

    @property
    def get_serial_number(self) -> int:
        return self._serial_number

