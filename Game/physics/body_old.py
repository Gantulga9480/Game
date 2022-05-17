from Game.graphic.cartesian import CartesianPlane
from Game.graphic.shapes import polygon
from Game.graphic import Vector2d
from math import pi

STATIC = 0
DYNAMIC = 1
FREE = 2


class body:

    def __init__(self, state, radius) -> None:
        super(body, self).__init__()
        self.state = state
        self.radius = radius

    def step(self):
        ...


class static_body(body):

    def __init__(self, radius) -> None:
        super(static_body, self).__init__(STATIC, radius)


class dynamic_body(body):

    def __init__(self, space, radius, dynamic) -> None:
        super(dynamic_body, self).__init__(DYNAMIC, radius)
        self.acceleration = Vector2d(space, 1, 0, max_length=10)
        self.velocity = Vector2d(space, 1, 0, max_length=200)
        self.dynamic = dynamic

    def step(self, *args):
        self.dynamic(self, *args)


class base_body(polygon):

    def __init__(self,
                 body_type,
                 pos: Vector2d,
                 vertex_count: int = 2,
                 size: float = 1,
                 limit_vertex: bool = True,
                 dynamic=None) -> None:
        parent = CartesianPlane((size, size), 1, pos)
        super().__init__(parent_space=parent,
                         vertex_count=vertex_count,
                         size=size,
                         limit_vertex=limit_vertex)
        self.body_type = body_type
        if body_type == STATIC:
            self.body = static_body(size)
        elif body_type == DYNAMIC:
            self.body = dynamic_body(parent, size, dynamic)
            self.body.acceleration.rotate(pi/2)
            self.body.velocity.rotate(pi/2)