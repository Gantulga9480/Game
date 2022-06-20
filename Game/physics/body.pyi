from Game.graphic.cartesian import CartesianPlane, Vector2d
from Game.graphic.shapes import Shape
from Game.math import point2d
from Game.color import BLACK
from pygame.color import Color
from typing import Union
import numpy as np


class object_body:
    type: int
    id: int
    radius: float
    friction_factor: float
    shape: Shape
    velocity: Vector2d
    collision_point: list[point2d]
    def __init__(self, id: int, type: int, vertex_count: int) -> None: ...
    def position(self) -> tuple: ...
    def speed(self) -> float: ...
    def step(self) -> None: ...
    def USR_step(self) -> None: ...
    def USR_resolve_collision(self, o: object_body, dxy: tuple) -> None: ...
    def attach(self, o: object_body, follow_dir: bool) -> None: ...
    def detach(self) -> None: ...
    def rotate(self, angle: float) -> None: ...
    def scale(self, factor: float) -> None: ...
    def show(self, color: Union[Color, tuple] = BLACK, show_vertex: bool = False) -> None: ...


class FreeBody(object_body):
    def __init__(self, id: int, plane: CartesianPlane, vertex_count: int) -> None: ...


class StaticBody(object_body):
    def __init__(self, id: int, plane: CartesianPlane, vertex_count: int) -> None: ...


class DynamicBody(object_body):
    def __init__(self, id: int, plane: CartesianPlane, vertex_count: int, max_speed: float = 1) -> None: ...
    def Accelerate(self, factor: float) -> None: ...


class DynamicPolygonBody(DynamicBody):
    def __init__(self, id: int, plane: CartesianPlane, size: tuple, max_speed: float = 1) -> None: ...


class DynamicRectangleBody(DynamicBody):
    def __init__(self, id: int, plane: CartesianPlane, size: tuple, max_speed: float = 1) -> None: ...


class DynamicTriangleBody(DynamicBody):
    def __init__(self, id: int, plane: CartesianPlane, sizes: list, max_speed: float = 1) -> None: ...


class StaticPolygonBody(StaticBody):
    def __init__(self, id: int, plane: CartesianPlane, size: tuple) -> None: ...


class StaticRectangleBody(StaticBody):
    def __init__(self, id: int, plane: CartesianPlane, size: tuple) -> None: ...


class StaticTriangleBody(StaticBody):
    def __init__(self, id: int, plane: CartesianPlane, sizes: list) -> None: ...


class FreePolygonBody(FreeBody):
    def __init__(self, id: int, plane: CartesianPlane, size: tuple) -> None: ...


class Ray(FreeBody):
    def __init__(self, id: int, plane: CartesianPlane, length: float) -> None: ...
