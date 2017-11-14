import pygame
import wave
import numpy
import math
import struct

pygame.init()
pygame.mixer.init()
# create display
screen_width = 800
screen_height = 600
pygame.display.set_mode((screen_width, screen_height))


pygame.mixer.music.load("MusicFile1.mp3") # play when kep pressed

explosion_sound = pygame.mixer.Sound("Explosion.wav")
explosion_samples = pygame.sndarray.samples(explosion_sound)
pygame.sndarray.make_sound(explosion_samples)




def change_volume(samples,volume_change):
    for sample in samples:
        numpy.multiply(sample, volume_change, out=sample, casting="unsafe")

def tone_generator():
    nchannels = 1
    sample_width = 2
    framerate = 44100
    nframes = framerate * 2
    frequency = 440
    sample_rate = 44100
    volume = 1
    bit_depth = 32767

    file = 'new_file'
    noise_out = wave.open(file, 'w')
    noise_out.setparams((nchannels, sample_width, framerate, nframes))
    values = []
    for i in range(0,sample_width):
        value = math.sin(2.0 * math.pi * frequency * (i / sample_rate)) * (volume * bit_depth)
        packaged_value = struct.pack("<h", value)
        for j in xrange(0, nchannels):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.write(value_str)

    noise_out.close()



running = True
music_volume = 0.5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tone_generator()


    pygame.display.update()

pygame.quit()

