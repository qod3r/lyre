import sys, os
import keyboard as kb
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from pprint import pprint
import pygame

from player import Player


basedir = os.path.dirname(__file__)

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(basedir, './resources/main.ui'), self)
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.init()
        pygame.mixer.set_num_channels(50)
        pygame.init()
        
        self.tracks = {}
        self.tracksl = []
        
        self.btnAdd.clicked.connect(self.addTrackFile)
        self.btnDelete.clicked.connect(self.deleteTrack)
        self.btnPlay.clicked.connect(self.playTrack)
    
    def deleteTrack(self):
        title = self.trackList.currentItem()
        if title is None:
            return
        title = title.text()
        
        idx = self.tracksl.index(title)
        del self.tracksl[idx]

        self.trackList.takeItem(idx)
        del self.tracks[title]
            
    def playTrack(self):
        title = self.trackList.currentItem()
        vol = self.sliderVolume.sliderPosition()
        if title is None:
            self.player = Player("", vol)
        else: 
            self.player = Player(self.tracks[title.text()], vol)
        self.player.show()
    
    def addTrack(self, fnames: list):
        text = []
        for fname in fnames:
            with open(fname, 'r') as f:
                text = f.read()
                title = fname.split('/')[-1].split('.')[0]
                self.tracks[title] = text
                self.tracksl.append(title)
                self.trackList.addItem(title)
    
    def addTrackFile(self):
        fname, ok = QFileDialog.getOpenFileName(
            self, 'Выбрать файл', '',
            'Текстовый файл (*.txt);;Все файлы (*)')
        if ok:
            self.addTrack([fname])
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        self.addTrack(files)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())