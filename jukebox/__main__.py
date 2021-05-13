import time
import logging
import json
from pathlib import Path

import gpiozero
import pygame

from mfrc522 import SimpleMFRC522


logging.basicConfig()
logger = logging.getLogger("jukebox")
logger.setLevel(logging.INFO)


amplifier = gpiozero.OutputDevice(21, active_high=True, initial_value=False)


reader = SimpleMFRC522()

LIBRARY = Path("/var/lib/jukebox")

with open(LIBRARY / "config.json") as f:
    SONGS = json.load(f)

pygame.mixer.init()
current_id = None
while True:
    for i in range(2):
        id = reader.read_id_no_block()
        if id is not None:
            break
        time.sleep(0.1)

    if id:
        if id not in SONGS:
            logger.warning(f"unkonwn id {id}")
            id = 0
        logger.info(f"ID: {id}, current_id: {current_id}, {pygame.mixer.music.get_busy()}")
        if id != current_id:
            current_id = id
            logger.info(f"Playing song {SONGS[id]}")

            pygame.mixer.music.load(SONGS[id])
            pygame.mixer.music.set_volume(1)
            amplifier.on()
            pygame.mixer.music.play()
        if not pygame.mixer.music.get_busy():
            # amplifier.off()
            pass
    else:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        #amplifier.off()
        logger.info("Reseting id")
        current_id = None
