import sys, os
import keyboard as kb
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from pprint import pprint
import pygame

basedir = os.path.dirname(__file__)


class Player(QWidget):
    def __init__(self, text, volume):
        super().__init__()
        uic.loadUi(os.path.join(basedir, './resources/player.ui'), self)
        # ui stuff
        self.btnExit.clicked.connect(self.back)
        self.btnPause.clicked.connect(self.pause)
        self.label.setText(text)
        
        self.text = text
        self.idx = 0
        
        # sound stuff
        self.volume = volume
        self.keys_str = "qwertyuasdfghjzxcvbnm"
        self.keys_ru = "йцукенгфывапроячсмить"
        self.curr_channel = 0
        self.init_sounds()
        self.init_keys()
        
        self.paused = False
        kb.add_hotkey("shift+right shift", self.pause)

    def back(self):
        self.paused = True
        # kb.remove_all_hotkeys()
        self.close()
    
    def pause(self):
        self.paused = not self.paused

    def init_sounds(self):
        self.sounds = {}
        for i in range(21):
            s = pygame.mixer.Sound(os.path.join(basedir, f"./resources/audio/lyre/{i}.wav"))
            s.set_volume(self.volume/100)
            self.sounds[self.keys_str[i]] = s
            self.sounds[self.keys_ru[i]] = s

    def track_notes(self):
        colorstart = '<font color="green">'
        colorend = '</font>'
        # while self.text[self.idx] != "-":
            
        newtext = colorstart + self.text[:self.idx] + colorend + self.text[self.idx:]
        self.label.setText(newtext)
        self.idx += 1

    def play(self, event):
        if self.paused:
            return
        
        pygame.mixer.Channel(self.curr_channel).play(self.sounds[str.lower(event.name)])
        # self.track_notes()
        self.curr_channel += 1
        if self.curr_channel >= 50:
            self.curr_channel = 0
        # print(event.name)

    def init_keys(self):
        self.listeners = {}
        for key in self.keys_str:
            self.listeners[key] = kb.on_press_key(key, self.play)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Player()
    ex.show()
    sys.exit(app.exec_())