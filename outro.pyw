import os
import sys
import time

import pygame
from pygame import mixer
from pynput.keyboard import Key, Controller

keyboard = Controller()

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

shutdown_for_real = False if len(sys.argv) > 1 else True

if os.name == 'nt':
    font = pygame.font.SysFont("Segoe UI", 72)
else:
    font = pygame.font.SysFont("Cantarell", 72)

if shutdown_for_real:
    music = os.path.join(os.getcwd(), 'outro.mp3')
    mixer.init()
    mixer.music.load(music)
    mixer.music.play()

frame_counter = 0
fps = 60

sec_before_shutdown = 13 if shutdown_for_real else 2

while True:
    if shutdown_for_real and frame_counter < 100:
        keyboard.press(Key.media_volume_up)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    screen.fill((0, 0, 0))

    time_left = sec_before_shutdown - int(frame_counter / fps)

    if time_left == 0:
        text = font.render("Shutting down ...", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

        screen.blit(text, text_rect)
        pygame.display.update()

        time.sleep(1)

        if shutdown_for_real:
            if os.name == "nt":
                os.system("shutdown.exe -p")
            else:
                os.system("sudo shutdown -h now")
        break

    text = font.render("System shutting down in " + str(time_left), True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

    screen.blit(text, text_rect)
    pygame.display.update()

    clock.tick(fps)
    frame_counter = frame_counter + 1

pygame.quit()
quit()
