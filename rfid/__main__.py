import time
import RPi.GPIO as GPIO
import pygame

from mfrc522 import SimpleMFRC522


reader = SimpleMFRC522()

SONGS = {
    
    365993536163: "/home/enick/phonybox_songs/deti-online.com_-_nichego-na-svete-luchshe-netu-01.mp3",
    42129601901: "/home/enick/phonybox_songs/malyshariki.mp3",
    0: "/home/enick/phonybox_songs/zainka.mp3",
        }

while True:
    id, text = reader.read()
    if id not in SONGS:
        print(f"unkonwn id {id}")
        id = 0

    print(f"Playing song {SONGS[id]}")

    pygame.mixer.init()
    pygame.mixer.music.load(SONGS[id])
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
