from typing import Optional

from Position import Position

class Direction():
    """Направление."""

    def __init__(self, image: Optional[str] = None, next: Optional[Position] = None) -> None:
        self._image = image
        self._next = next

    @property
    def image(self):
        """Возвращает ссылку на изображение направления."""
        return self._image

    @property
    def next(self):
        """Возвращает ссылку на следующую позицию."""
        return self._next

