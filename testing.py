import keyboard as kb
import pygame

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("resources/audio/lyre/0.wav")

def play():
    print("a")
    pygame.mixer.music.play()

kb.add_hotkey('a', play)
kb.wait()