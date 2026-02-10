import pygame
import os
import time
import RPi.GPIO as GPIO #type: ignore
from gpiozero import Button
from pygame import mixer
from pygame import KEYDOWN, K_q, K_RIGHT, K_LEFT, K_UP, K_h


"""
Things to do:
Bind Buttons
Make Rig for Audio Player
Go to walmart for a tiny speaker
Get filament for 3D printer
"""

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.init()
mixer.init()


folder_path = "/home/pi/Documents/PiBoardProject/MusicAssets/"


class Audio():
    def __init__(self, songName, audioVolume):
        self.songName = songName
        self.volume = pygame.mixer_music.set_volume(audioVolume)
        pass
    def PlayAudio(self):
        pygame.mixer_music.load(os.path.join(folder_path, self.songName))
        pygame.mixer_music.play()
    def StopAudio(self):
        pygame.mixer_music.stop()
    def QueueNext(self):
        pygame.mixer_music.queue(os.path.join(folder_path, self.songName))

audios = []

for filename in os.listdir(folder_path):
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        audio = Audio(filename, 1.0)
        audios.append(audio)


for audio in audios:
    print(audios.index(audio) + 1, audio.songName)


audioPlaying = 1


def PauseMusic():
    time.sleep(0.5)
    pygame.mixer_music.pause() if pygame.mixer_music.get_busy() else pygame.mixer_music.unpause()

def NextSong():
    audios[audioPlaying - 1].StopAudio()
    if audioPlaying >= len(audios):
            audioPlaying = 1
    else:
        audioPlaying += 1
    time.sleep(1)
    print(f"Now playing: {audios[audioPlaying - 1].songName}")
    audios[audioPlaying - 1].PlayAudio()

def PreviousSong():
    audios[audioPlaying - 1].StopAudio()
    if audioPlaying <= 1:
            audioPlaying = len(audios)
    else:
        audioPlaying -= 1
    time.sleep(1)
    print(f"Now playing: {audios[audioPlaying - 1].songName}")
    audios[audioPlaying - 1].PlayAudio()

audios[audioPlaying - 1].PlayAudio()


print("Left (-) or Right (+) to change songs, Up to play/pause, Q to quit, H for this message to show again")


window = pygame.display.set_mode((300, 300))


def StoreCode():
    """
    if event.key == pygame.K_RIGHT:
                if audioPlaying <= 1:
                    audioPlaying = len(audios)
                else:
                    audioPlaying -= 1
                time.sleep(1)
                print(f"Now playing: {audios[audioPlaying - 1].songName}")
                audios[audioPlaying - 1].PlayAudio()
            elif event.key == pygame.K_LEFT:
                if audioPlaying >= len(audios):
                    audioPlaying = 1
                else:
                    audioPlaying += 1
                audios[audioPlaying - 1].StopAudio()
                time.sleep(1)
                print(f"Now playing: {audios[audioPlaying - 1].songName}")
                audios[audioPlaying - 1].PlayAudio()
            elif event.key == pygame.K_UP:
                pygame.mixer_music.pause() if pygame.mixer_music.get_busy() else pygame.mixer_music.unpause()
            elif event.key == pygame.K_h:
                print("Left (-) or Right (+) to change songs, Up to play/pause, Q to quit, H for this message to show again")
    """
    """
    
    keys = pygame.key.get_pressed()


    if keys[K_LEFT]:
        if audioPlaying <= 1:
            audioPlaying = len(audios)
        else:
            audioPlaying -= 1
        time.sleep(1)
        print(f"Now playing: {audios[audioPlaying - 1].songName}")
        audios[audioPlaying - 1].PlayAudio()
    elif keys[K_RIGHT]:
        if audioPlaying >= len(audios):
            audioPlaying = 1
        else:
            audioPlaying += 1
        audios[audioPlaying - 1].StopAudio()
        time.sleep(1)
        print(f"Now playing: {audios[audioPlaying - 1].songName}")
        audios[audioPlaying - 1].PlayAudio()
    elif keys[K_UP]:
        time.sleep(0.5)
        pygame.mixer_music.pause() if pygame.mixer_music.get_busy() else pygame.mixer_music.unpause()
    elif keys[K_h]:
        print("Left (-) or Right (+) to change songs, Up to play/pause, Q to quit, H for this message to show again")
        """
"""
buttonPause.when_pressed = PauseMusic
buttonNext.when_pressed = NextSong
buttonPrev.when_pressed = PreviousSong
"""

try:
    audioPlaying = 1
    isAudioPlaying = True
    def EyesON(playing):
        playing = True
        print("EyesOn")
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
    def EyesOFF(playing):
        playing = False
        print("EyesOff")
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
    
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    isAudioPlaying = True
    while True:
        if GPIO.input(13) == GPIO.LOW:
            EyesOFF(isAudioPlaying)
            audios[audioPlaying - 1].StopAudio()
            if audioPlaying >= len(audios):
                audioPlaying = 1
            else:
                audioPlaying += 1
            time.sleep(1)
            EyesON(isAudioPlaying)
            print(f"Now playing: {audios[audioPlaying - 1].songName}")
            audios[audioPlaying - 1].PlayAudio()
            time.sleep(1)
        elif GPIO.input(19) == GPIO.LOW:
            PauseMusic()
            if isAudioPlaying:
                EyesOFF(isAudioPlaying)
            else:
                EyesON(isAudioPlaying)
            time.sleep(1)
        elif GPIO.input(26) == GPIO.LOW:
            audios[audioPlaying - 1].StopAudio()
            EyesOFF(isAudioPlaying)
            if audioPlaying <= 1:
                audioPlaying = len(audios)
            else:
                audioPlaying -= 1
            EyesON(isAudioPlaying)
            print(f"Now playing: {audios[audioPlaying - 1].songName}")
            audios[audioPlaying - 1].PlayAudio()
            time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
finally:
    GPIO.cleanup()

"""loop = True
while loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_q:
            loop = False
            break
        elif event.type == pygame.mixer_music.get_endevent():
            print("Song Ended")
            if audioPlaying >= len(audios):
                audioPlaying = 1
            else:
                audioPlaying += 1
            audios[audioPlaying - 1].PlayAudio()
            print(f"Now playing: {audios[audioPlaying - 1].songName}")
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            print(event.key)"""