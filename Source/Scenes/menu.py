from Source.Scenes.base import BaseScene
from Source.BaseClasses.text import Text
from Source.Objects.start_game_button import StartGameButton
from Source.Objects.highscores_button import HighscoreButton
from Source.Objects.settings_button import SettingsButton
from Source.BaseClasses.image import Image


class MenuScene(BaseScene):
    def __init__(self):
        self.title = Text("Defend the Base", "Candara", 100, (255, 255, 255), 549.5, 200)
        self.credit_text = Text("Created by Foxycoder and Atoroe", "Candara", 15, (0, 0, 0), 20, 850)
        self.credit_text_2 = Text("Artworks by xianxian's dumpling", "Candara", 15, (0, 0, 0), 20, 870)
        self.version_text = Text("Development version", "Candara", 15, (0, 0, 0), 1650, 870)
        self.start_game_button = StartGameButton(800, 350, 70, 200, "Candara", (255, 255, 255), 30, "Start Game", (50, 30, 100), (70, 50, 120), True, (70, 50, 120), 5)
        self.highscores_button = HighscoreButton(800, 430, 70, 200, "Candara", (255, 255, 255), 30, "Highscores", (50, 30, 100), (70, 50, 120), True, (70, 50, 120), 5)
        self.settings_button = SettingsButton(800, 510, 70, 200, "Candara", (255, 255, 255), 30, "Settings", (50, 30, 100), (70, 50, 120), True, (70, 50, 120), 5)
        self.bg_image = Image(filename="Assets/Images/Menu background.png", x=0, y=0, resize=150)
        super().__init__()
        self.objects.append(self.bg_image)
        self.objects.append(self.title)
        self.objects.append(self.credit_text)
        self.objects.append(self.credit_text_2)
        self.objects.append(self.version_text)
        self.objects.append(self.start_game_button)
        self.objects.append(self.highscores_button)
        self.objects.append(self.settings_button)

    def logic(self):
        self.check_close()
        for object in self.objects:
            if object == self.start_game_button and object.logic() == "nextscene":
                return "nextscene"
            elif object == self.highscores_button and object.logic() == "highscores":
                return "highscores"
            elif object == self.settings_button and object.logic() == "settingscene":
                return "settingscene"


