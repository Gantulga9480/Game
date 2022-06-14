from Game import Game
from Game.graphic import CartesianPlane
from Game.physics import DynamicPolygonBody, StaticPolygonBody
import pygame as pg


class Test(Game):

    def __init__(self) -> None:
        super().__init__(width=1920, height=1080, flags=pg.FULLSCREEN | pg.HWSURFACE)
        self.plane = CartesianPlane(self.window, (self.width, self.height))
        p = self.plane.createPlane()
        self.d = DynamicPolygonBody(1, p, (30, 0), 10)
        self.s = DynamicPolygonBody(0, p.createPlane(y=30), (50, 50, 50, 1, 1, 1, 50, 50), 10)
        self.s.attach_to(self.d, True)
        self.mainloop()

    def USR_eventHandler(self, event):
        if event.type == pg.KEYUP:
            if event.key == pg.K_q:
                self.running = False

    def USR_loop(self):
        if self.keys[pg.K_UP]:
            self.d.Accelerate(0.5)
        elif self.keys[pg.K_DOWN]:
            self.d.Accelerate(-0.5)
        if self.keys[pg.K_LEFT]:
            self.d.rotate(0.1)
        elif self.keys[pg.K_RIGHT]:
            self.d.rotate(-0.1)

        if self.keys[pg.K_w]:
            self.s.Accelerate(0.5)
        elif self.keys[pg.K_s]:
            self.s.Accelerate(-0.5)
        if self.keys[pg.K_a]:
            self.s.rotate(0.1)
        elif self.keys[pg.K_d]:
            self.s.rotate(-0.1)

        if self.keys[pg.K_z]:
            self.s.attach_to(self.d, True)
        elif self.keys[pg.K_c]:
            self.s.detach()

        self.d.step()
        self.s.step()

    def USR_render(self):
        self.d.show((255, 0, 0))
        self.s.show((0, 0, 0))


Test()
