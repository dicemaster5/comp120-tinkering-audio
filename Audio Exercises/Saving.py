import pygame
import wave
import numpy

def change_volume(samples,volume_change):
    for sample in samples:
        sample *= volume_change

pygame.init()
pygame.mixer.init()
# create display
screen_width = 800
screen_height = 600
pygame.display.set_mode((screen_width, screen_height))

pygame.mixer.music.load("bensound-scifi.mp3") # play when kep pressed

explosion_sound = pygame.mixer.Sound("Explosion.wav")
explosion_samples = pygame.sndarray.samples(explosion_sound)

def save_snd(sound_file):
    sound = pygame.mixer.Sound(sound_file)

    sound_samples = pygame.sndarray.samples(sound)
    new_sound_array = change_volume(sound_samples, 10000)
    new_sound = pygame.sndarray.make_sound(new_sound_array)
    new_sound = sound.get_raw()

    file = wave.open("editedsound.wav", "w")
    file.write(new_sound)
    file.close()
    #new_file = raw_input("") + ".wav"
    #pygame.mixer.save(new_sound, ("new_sound.wav"))

    # open new wave file
    #sfile = wave.open('white_noise.wav', 'w')



    # write raw PyGame sound buffer to wave file
    sfile.writeframesraw(new_sound.get_buffer().raw)

    # close file
    sfile.close()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                explosion_sound.play()
            if event.key == pygame.K_UP:
                change_volume(explosion_samples, 10000)
            if event.key == pygame.K_q:
                pygame.mixer.music.play()
            if event.key == pygame.K_w:
                pygame.mixer.music.stop()
            if event.key == pygame.K_s:
                save_snd(explosion_sound)


    pygame.display.update()

pygame.quit()

