import sys
import keyboard as kb
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QSound, QSoundEffect
from PyQt5.QtCore import QUrl
from pprint import pprint
import pygame


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        pygame.mixer.set_num_channels(50)
        pygame.init()
        
        self.keys_str = "qwertyuasdfghjzxcvbnm"
        self.curr_channel = 0
        self.init_sounds()
        self.init_keys()

    def init_sounds(self):
        self.sounds = {}
        for i in range(21):
            s = pygame.mixer.Sound(f"./resources/audio/lyre/{i}.wav")
            s.set_volume(0.5)
            self.sounds[self.keys_str[i]] = s

    def play(self, event):
        # self.sounds[event.name].stop()
        # self.sounds[event.name].play()
        # pygame.mixer.music.load(f"./resources/audio/lyre/{self.keys_str.index(event.name)}.wav")
        # pygame.mixer.music.play()
        
        pygame.mixer.Channel(self.curr_channel).play(self.sounds[event.name])
        self.curr_channel += 1
        if self.curr_channel >= 50:
            self.curr_channel = 0
    
    def init_keys(self):
        self.listeners = {}
        for key in self.keys_str:
            self.listeners[key] = kb.on_press_key(key, self.play) 
        
    def handle(self):
        # self.book.addItem(f"{self.name.text()} - {self.phone.text()}")
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())