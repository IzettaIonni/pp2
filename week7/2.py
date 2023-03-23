from multiprocessing.connection import wait
import pygame
from os import listdir


def play():
    global song_name, song_name_rect
    pygame.mixer.music.load(path + '\\' + music[now_playing])
    song_name = font.render(music[now_playing], True, (255, 90, 90))
    song_name_rect = song_name.get_rect(center=(200, 100))
    pygame.mixer.music.play()


def next():
    global now_playing, song_name, song_name_rect
    now_playing += 1
    pygame.mixer.music.unload()
    pygame.mixer.music.load(path + '\\' + music[now_playing])
    song_name = font.render(music[now_playing], True, (255, 90, 90))
    song_name_rect = song_name.get_rect(center=(200, 100))
    pygame.mixer.music.play()


def prev():
    global now_playing, song_name, song_name_rect
    now_playing -= 1
    pygame.mixer.music.unload()
    pygame.mixer.music.load(path + '\\' + music[now_playing])
    song_name = font.render(music[now_playing], True, (255, 90, 90))
    song_name_rect = song_name.get_rect(center=(200, 100))
    pygame.mixer.music.play()


pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("music player")
font = pygame.font.SysFont("comicsans", 20)
pygame.mixer.music.set_volume(0.15)

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

path = "week7\music"
music = listdir(path)
now_playing = 0

play()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == SONG_END:
            if now_playing < len(music)-1:
                now_playing += 1
                play()
            else:
                done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_LEFT:
                if now_playing > 0:
                    prev()
            if event.key == pygame.K_RIGHT:
                if now_playing < len(music)-1:
                    next()

    screen.fill((0, 0, 0))
    screen.blit(song_name, song_name_rect)
    pygame.display.flip()

pygame.quit()
