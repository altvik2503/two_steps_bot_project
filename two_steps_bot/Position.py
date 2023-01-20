from typing import List, Union, Tuple, Iterable
from dataclasses import dataclass, field

from Direction import Direction


@dataclass
class Position():
    """Точка остановки."""

    directions: List[Direction] = field(default_factory=list)
    selected: int = 0

    @property
    def _size(self) -> int:
        """Возвращает количество напрпавлений."""
        return len(self.directions)

    @property
    def image(self):
        """Возвращает изображение активного направления."""
        return self.directions[self.selected].image

    @property
    def next(self):
        """Возвращает ссылку на следующую позицию активного направления."""
        return self.directions[self.selected].next

    def _rotate(self, step: int) -> None:
        """Поворачивает текущее направление до активного (с изображением)."""
        for _ in range(self._size):
            self.selected = (self.selected + step) % self._size
            if self.image:
                break

    def left(self) -> None:
        """Поворачивает текущее направление налево."""
        self._rotate(-1)

    def right(self) -> None:
        """Поворачивает текущее направление направо."""
        self._rotate(1)

    def add(self,
        directions: Union['Direction',
        Iterable['Direction']]
    ) -> None:
        """Добавляет направление в конец списка направлений позиции."""
        if isinstance(directions, Iterable):
            self.directions.extend(directions)
        else:
            self.directions.append(directions)
