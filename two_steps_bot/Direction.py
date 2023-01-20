from typing import Optional
from dataclasses import dataclass

from Position import Position

@dataclass
class Direction():
    """Определяет параметры направления перемещения из позиции."""
    image: Optional[str] = None
    next: Optional[Position] = None
