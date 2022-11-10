from Direction import Direction
from Tour import Tour
from Position import Position
from settings import STATIC


IMAGE_TEMPLATE = STATIC.join('{}.jpg')

head = Position()
point_1 = Position()
point_2 = Position()

head.add([
    Direction(IMAGE_TEMPLATE.format('1F'), point_1),
    Direction(IMAGE_TEMPLATE.format('1R')),
    Direction(IMAGE_TEMPLATE.format('1B')),
    Direction(IMAGE_TEMPLATE.format('1L')),
])

point_1.add([
    Direction(IMAGE_TEMPLATE.format('2F')),
    Direction(IMAGE_TEMPLATE.format('2R')),
    Direction(IMAGE_TEMPLATE.format('2B'), head),
    Direction(IMAGE_TEMPLATE.format('2L'), point_2),
])

point_2.add([
    Direction(IMAGE_TEMPLATE.format('3F')),
    Direction(IMAGE_TEMPLATE.format('3B'), point_1),
])
