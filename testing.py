import keyboard as kb
from pprint import pprint
import pygame

# pygame.mixer.pre_init(44100, -16, 2, 2048)
# pygame.mixer.init()
# pygame.init()
# pygame.mixer.music.load("resources/audio/lyre/0.wav")

# def play(a):
#     print("a")
#     pygame.mixer.music.play()

# kb.hook(play)
# kb.add_hotkey('a', lambda a: play(a))
# kb.wait()

def play():
    print("asd")

kb.add_hotkey("shift+right shift", play)
kb.wait()