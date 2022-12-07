from Source.Scenes.base import BaseScene
from Source.BaseClasses.text import Text
from Source.Objects.start_game_button import StartGameButton

class MenuScene(BaseScene):
    def __init__(self):
        self.title = Text("Defend the Base", "Candara", 100, (255, 255, 255), 549.5, 200)
        self.credit_text = Text("Created by Foxycoder and Atoroe", "Candara", 15, (255, 255, 255), 20, 850)
        self.credit_text_2 = Text("Artworks by xianxian's dumpling", "Candara", 15, (255, 255, 255), 20, 870)
        self.version_text = Text("Development version", "Candara", 15, (255, 255, 255), 1650, 870)
        self.start_game_button = StartGameButton(800, 350, 70, 200, "Candara", (255, 255, 255), 30, "Start Game", (50, 30, 100), (70, 50, 120), True, (70, 50, 120), 5)
        super().__init__()
        self.objects.append(self.title)
        self.objects.append(self.credit_text)
        self.objects.append(self.credit_text_2)
        self.objects.append(self.version_text)
        self.objects.append(self.start_game_button)

    def logic(self):
        for object in self.objects:
            if object == self.start_game_button and object.logic() == "nextscene":
                return "nextscene"
