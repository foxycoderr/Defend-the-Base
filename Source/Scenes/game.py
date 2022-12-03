from Source.Scenes.base import BaseScene
import pygame
from Source.settings import Settings
from Source.Objects.monster_base import MonsterBase


class GameScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.path = [[56, 584], [152, 641], [349, 465], [509, 504], [500, 645], [550, 720], [700, 700], [802, 610], [740, 368], [830, 260], [1000, 400], [1070, 550], [1250, 610], [1430, 475], [1460, 367], [1545, 344], [1620, 415], [1640, 514], [1750, 550], [1800, 516]]
        self.monster1 = MonsterBase(self.path)
        self.monster2 = MonsterBase(self.path)
        self.monster3 = MonsterBase(self.path)
        self.progress = [0, 0, 0]
        self.objects.append(self.monster1)
        self.objects.append(self.monster2)
        self.objects.append(self.monster3)



