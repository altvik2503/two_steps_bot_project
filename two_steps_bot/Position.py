from typing import List, Union, Tuple

from Direction import Direction


class Position():
    """Точка остановки."""

    def __init__(self, directions: List[Direction] = []) -> None:
        self._directions = directions
        self._active = 0

    @property
    def _size(self) -> int:
        """Возвращает количество напрпавлений."""
        return len(self._directions)

    @property
    def image(self):
        """Возвращает изображение активного направления."""
        return self._directions[self._active].image

    @property
    def next(self):
        """Возвращает ссылку на следующую позицию активного направления."""
        return self._directions[self._active].next

    def _rotate(self, step: int) -> None:
        """Поворачивает текущее направление до активного (с изображением)."""
        for _ in range(self._size):
            self._active = (self._active + step) % self._size
            if self.image:
                break

    def left(self) -> None:
        """Поворачивает текущее направление налево."""
        self._rotate(-1)

    def right(self) -> None:
        """Поворачивает текущее направление направо."""
        self._rotate(1)

    def add(self, directions: Union['Direction', List['Direction']]) -> None:
        if isinstance(directions, (List, Tuple)):
            self._directions.extend(directions)
        else:
            self._directions.append(directions)

