import pygame
import wave
import numpy
import math
import struct
import random

pygame.init()
pygame.mixer.init()

SAMPLE_WIDTH = 2
SAMPLE_RATE = 44100.0
BIT_DEPTH = 2.0
CHANNELS = 2

# dictionary for the various notes, two octaves currently
notes = {"A": 0, "A#": 1, "B": 2, "C": 3, "C#": 4, "D": 5, "D#": 6, "E": 7,
         "F": 8, "F#": 9, "G": 10, "G#": 11, "a": 12, "a#": 13, "b": 14,
         "c": 15, "c#": 16, "d": 17, "d#": 18, "e": 19, "f": 20, "f#": 21,
         "g": 22, "g#": 23}




def change_volume(samples,volume_change):
    for sample in samples:
        numpy.multiply(sample, volume_change, out=sample, casting="unsafe")


'''This function generates a tone'''

def generate_tone_from_string(note, sample_rate, seconds, volume):
    values = []
    frequency = 440.0 * 2.0 ** (notes[note] / 12.0)
    sample_length = int(seconds * 44100)
    for i in range(0, sample_length):
        value = math.sin(2 * math.pi * frequency * (i / sample_rate)) * \
                (volume * BIT_DEPTH)
        value_2 = 2 * (math.sin(frequency * (i / sample_rate)) *
                       (volume * BIT_DEPTH)) / -math.pi
        value_3 = 4 * (math.sin(frequency * (i / sample_rate)) *
                       (volume * BIT_DEPTH)) / math.pi
        for j in xrange(0, CHANNELS):
            #values.append(value)
            #values.append(value_2)
            values.append(value_3)

    return values

'''This makes a random list of various notes from the dictionary'''

random_music = []

# you can choose the number of notes that will be played
def generate_random_music(number_of_notes):
    current_number_of_notes = 0
    while number_of_notes > current_number_of_notes:
        # creates a list called random_music out of the notes in the dictionary
        random_music.append(random.choice(notes.keys()))
        current_number_of_notes += 1
    print random_music


'''This function uses the tone generator to create the music samples '''

data_to_save = []

def write_melody(list_of_notes):
    data_to_save.extend(generate_tone_from_string
                        (list_of_notes[0], SAMPLE_RATE, random.choice
                        ([0.2, 0.2, 0.4, 0.6, 1, 0.4 ]), 1000.0))
    for note in list_of_notes[1:]:
        data_to_save.extend(generate_tone_from_string
                            (note, SAMPLE_RATE, random.choice
                            ([0.2, 0.2, 0.4, 0.6, 1, 0.4 ]), 1000.0))


'''This function saves the data as a wav file'''

def save_melody(wav_data, name_of_file):
    packed_values = []
    for i in range(0, len(wav_data)):
        packed_value = struct.pack('h', wav_data[i])
        packed_values.append(packed_value)

    noise_out = wave.open(name_of_file, 'w')
    noise_out.setparams((CHANNELS, SAMPLE_WIDTH, SAMPLE_RATE, 0,
                         'NONE', 'not compressed'))
    value_str = ''.join((str(n) for n in packed_values))
    noise_out.writeframes(value_str)
    noise_out.close()


pre_written_melody = ['D', 'F', 'd', 'D', 'F', 'd', 'e', 'f', 'e', 'f',
                      'e', 'c', 'A', 'A', 'D', 'F', 'G', 'A', 'A', 'D',
                      'F', 'G', 'E']

# number of notes can be changed, also changes the music length
generate_random_music(20)

write_melody(random_music)

save_melody(data_to_save, "newMelody.wav")
