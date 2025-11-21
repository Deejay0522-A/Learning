#SpeakerCode by Dee Lopez
#Named main.py because of pygame needing a main file to go off

#Manage the imports
import pygame
import os
import time
from pygame import mixer
from pygame import KEYDOWN, K_q, K_RIGHT, K_LEFT, K_UP, K_h

# Initalize Pygame
pygame.init()
mixer.init()

# Map the folder path so that the OS makes sure to go to the folder with your music
# make sure the \ turns into \\
folder_path = "C:\\Users\\deeja\\Downloads\\Abaddon-main\\Abaddon-main\\My project\\Assets\\Scripts\\Github\\Learning\\Python\\Speaker\\Assets"

# Create the class of Audio
class Audio():
    # The initalization allows for the songs to have a name and volume
    def __init__(self, songName, audioVolume):
        self.songName = songName
        self.volume = pygame.mixer_music.set_volume(audioVolume)
        pass
    #These 3 functions are binded to the buttons which allow for them to play audio according to your input
    def PlayAudio(self):
        pygame.mixer_music.load(os.path.join(folder_path, self.songName))
        pygame.mixer_music.play()
    def StopAudio(self):
        pygame.mixer_music.stop()
    def QueueNext(self):
        pygame.mixer_music.queue(os.path.join(folder_path, self.songName))

# List for audios
audios = []

# For loop creating the list of songs
for filename in os.listdir(folder_path):
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        audio = Audio(filename, 1.0)
        audios.append(audio)

# Prints the list of audios within the list
for audio in audios:
    print(audios.index(audio) + 1, audio.songName)

# This maps which song within the list the program plays
audioPlaying = 1

# This is -1 because of the range being 1-7 instead of the usual list 0-6
audios[audioPlaying - 1].PlayAudio()

# Prints the controls of the program
print("Left (-) or Right (+) to change songs, Up to play/pause, Q to quit, H for this message to show again")

# ONLY NEEDED FOR COMPUTER NOT GPIO, THIS IS THE PC CODE
window = pygame.display.set_mode((300, 300))

# Just a way to store past code that worked
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

#Creating the loop
loop = True
while loop:
    # Getting the events pygame provides
    for event in pygame.event.get():
        # Quits if X is clicked or if Q is pressed
        if event.type == pygame.QUIT or event.type == pygame.K_q:
            loop = False
            break
        # Plays next song if current one has ended
        elif event.type == pygame.mixer_music.get_endevent():
            print("Song Ended")
            #If statements check if the audio is the last song or not, restarting the list from the first song
            if audioPlaying >= len(audios):
                audioPlaying = 1
            else:
                audioPlaying += 1
            audios[audioPlaying - 1].PlayAudio()
            print(f"Now playing: {audios[audioPlaying - 1].songName}")
        #Prints key thats pressed
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            print(event.key)
   #Variable for the key events
    keys = pygame.key.get_pressed()

    #Binded functions to keys, Previous, Next, Pause, & Help in order
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
    
pygame.quit()