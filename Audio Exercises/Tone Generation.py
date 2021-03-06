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

'''This function generates a single tone'''
# The first tone to be created and played
def tone_generator():
    # Variables for the sound tone that will be created
    nchannels = 1
    sample_width = 2
    framerate = 44100
    nframes = framerate * 3
    frequency = 240
    sample_rate = 44100
    volume = 1
    bit_depth = 32767

    # Name of the file
    file = 'new_file.wav'
    # creates a wav file
    noise_out = wave.open(file, 'w')
    # sets wav file parameters
    noise_out.setparams((nchannels, sample_width, framerate, nframes, 'NONE', 'not compressed'))
    # creates an empty list to assign samples to later
    values = []
    # a loop to create samples using sine
    for i in range(0, nframes):
        value = math.sin(2.0 * math.pi * frequency * (float(i) / sample_rate)) * (volume * bit_depth)
        packaged_value = struct.pack("<h", value)
        for j in xrange(0, nchannels):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)

    noise_out.close()

# The second tone that gets gets created
def tone_generator_2():
    nchannels = 1
    sample_width = 2
    framerate = 44100
    nframes = framerate * 1
    frequency = 880
    frequency_2 = 440
    frequency_3 = 220
    frequency_4 = 1760
    sample_rate = 44100
    sample_rate2 = 33000
    volume = 1
    bit_depth = 32767

    # Name of the file
    file = 'new_file_2.wav'
    noise_out = wave.open(file, 'w')
    noise_out.setparams((nchannels, sample_width, framerate, nframes, 'NONE', 'not compressed'))
    values = []
    for i in range(0, nframes):
        value = math.sin(2.0 * math.pi * frequency * (float(i) / sample_rate)) * (volume * bit_depth)
        packaged_value = struct.pack("<h", value)
        for j in xrange(0, nchannels):
            values.append(packaged_value)
    for i in range(0, nframes):
        value = math.sin(2.0 * math.pi * frequency_2 * (float(i) / sample_rate2)) * (volume * bit_depth)
        packaged_value = struct.pack("<h", value)
        for j in xrange(0, nchannels):
            values.append(packaged_value)
    for i in range(0, nframes):
        value = math.sin(2.0 * math.pi * frequency_3 * (float(i) / sample_rate)) * (volume * bit_depth)
        packaged_value = struct.pack("<h", value)
        for j in xrange(0, nchannels):
            values.append(packaged_value)
    for i in range(0, nframes):
        value = math.sin(2.0 * math.pi * frequency_4 * (float(i) / sample_rate)) * (volume * bit_depth)
        packaged_value = struct.pack("<h", value)
        for j in xrange(0, nchannels):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)

    noise_out.close()


def echo(sound1,sound2,delay,sample_length):
    values=[]
    for i in range(0,sample_length):
        values.append(sound1[i])
        if i>delay:
            echo=sound1[i]*0.6
            values.append(echo+sound1[i])
    return values




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
                #tone_generator()
                #tone_generator_2()
                echo(new_file, new_file_2, 1, )

    pygame.display.update()

pygame.quit()

