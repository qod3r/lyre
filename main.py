import sys, os
import keyboard as kb
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from pprint import pprint
import pygame

basedir = os.path.dirname(__file__)

class DummyEvent:
    def __init__(self, name):
        self.name = name

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(basedir, './resources/main.ui'), self)
        
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        pygame.mixer.set_num_channels(50)
        pygame.init()
        
        self.keys_str = "qwertyuasdfghjzxcvbnm"
        self.keys_ru = "йцукенгфывапроячсмить"
        self.curr_channel = 0
        self.init_sounds()
        self.init_keys()
        self.init_buttons()
        
        self.paused = False
        kb.add_hotkey("shift+right shift", self.pause)

    def pause(self):
        self.paused = not self.paused

    def init_buttons(self):
        self.buttons = []
        btns = {
            0: 'do',
            1: 're',
            2: 'mi',
            3: 'fa',
            4: 'so',
            5: 'la',
            6: 'ti'
        }
        for i in range(21):
            b = QPushButton('', self)
            b.clicked.connect(self.play)
            b.setIcon(QIcon(os.path.join(basedir, f"./resources/icons/{btns[i % 7]}.svg")))
            b.name = self.keys_str[i]
            b.setIconSize(QSize(60, 60))
            self.gridLayout.addWidget(b, i // 7, i % 7, Qt.AlignHCenter | Qt.AlignVCenter)
            self.buttons.append(b)
    
    def init_sounds(self):
        self.sounds = {}
        for i in range(21):
            s = pygame.mixer.Sound(os.path.join(basedir, f"./resources/audio/lyre/{i}.wav"))
            s.set_volume(0.3)
            self.sounds[self.keys_str[i]] = s
            self.sounds[self.keys_ru[i]] = s
    
    def play(self, event):
        if self.paused:
            return
        if event == False:
            event = DummyEvent(self.sender().name)
            
        if len(self.label.text()) > 15:
            self.label.setText("")
        self.label.setText(self.label.text() + event.name)
            
        pygame.mixer.Channel(self.curr_channel).play(self.sounds[str.lower(event.name)])
        self.curr_channel += 1
        if self.curr_channel >= 50:
            self.curr_channel = 0
        print(event.name)

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