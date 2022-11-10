from typing import Optional, List, Union, Tuple
from telegram import (
    Update,
    ParseMode,
)
from telegram.ext import (
    Updater,
    Handler,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CallbackContext,
)


class Position():
    """Точка остановки."""

    def __init__(self, dimensions: List['Direction'] = []) -> None:
        self._dimentions = dimensions
        self._active = 0

    @property
    def _size(self) -> int:
        """Возвращает количество напрпавлений."""
        return len(self._dimentions)

    @property
    def image(self):
        """Возвращает изображение активного направления."""
        return self._dimentions[self._active].image

    @property
    def next(self):
        """Возвращает ссылку на следующую позицию активного направления."""
        return self._dimentions[self._active].next

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
            self._dimentions.extend(directions)
        else:
            self._dimentions.append(directions)


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


class Tour():
    """Продвигает пользователя по сети позиций."""

    def __init__(self, updater: Updater, head: Position) -> None:
        """Принимает бот и начальную позицию."""
        self._active = head
        self._updater = updater

    def _update(self) -> None:
        """Обновляет изобажение у пользователя."""
        pass

    def start(self):
        self._updater.start_polling()
        self._updater.idle()

    def stop(self):
        self._updater.stop()

    def step(self) -> None:
        """Переводит текущее положение в следующую позицию."""
        next = self._active.next
        if next:
            self._active = next
            self._update()

    def left(self) -> None:
        """Поворачивает влево."""
        self._active.left()
        self._update()

    def right(self) -> None:
        """Поворачивает вправо."""
        self._active.left()
        self._update()

    def add_handlers(self, handlers: Union[List[Handler], Handler]) -> None:
        if isinstance(handlers, (List, Tuple)):
            for handler in handlers:
                self._updater.dispatcher.add_handler(handler)
        else:
            self._updater.dispatcher.add_handler(handlers)

