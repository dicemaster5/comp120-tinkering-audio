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

# dictionary for the various notes, spans three octaves
'''
notes = {"iA": -12, "iA#": -11, "iB": -10, "iC": -9, "iC#": -8, "iD": -7,
         "iD#": -6, "iE": -5, "iF": -4, "iF#": -3, "iG": -2, "iG#": -1, "A": 0,
         "A#": 1, "B": 2, "C": 3, "C#": 4, "D": 5, "D#": 6, "E": 7,
         "F": 8, "F#": 9, "G": 10, "G#": 11, "a": 12, "a#": 13, "b": 14,
         "c": 15, "c#": 16, "d": 17, "d#": 18, "e": 19, "f": 20, "f#": 21,
         "g": 22, "g#": 23}
'''

dark_notes = {"iC": -9, "iD": -7, "iD#": -6, "iF": -4, "iG": -2, "A": 0, "B": 2}  # mysterious jazzy

exotic_notes = {"C": 3, "C#": 4, "E": 7, "F": 8, "G": 10, "G#": 11, "a#": 13}  # exotic, middle eastern

happy_notes = {"C": 3, "D": 5,"E": 7,"a": 12, "b": 14, "F": 8, "B": 2, "G": 10}  # major scale

blues_notes = {"iA": -12, "iA#": -11, "iB": -10, "iD": -7, "iE": -5, "iF": -4, "A": 0}  # blues

spanish_notes = {"C": 3, "C#": 4, "D#": 6, "F": 8, "G": 10, "G#": 11, "a#": 13}  # spanish/flamenco

dreamy_notes = {"C": 3, "D": 5, "E": 7, "F#": 9, "G#": 11, "a#": 13}  # dreamy/underwater

arpeggio_notes = {"iA": -12, "iC#": -8, "iE": -5, "iG#": -1, "A": 0,}  # Arpeggio

dict = int(raw_input("Pick a genre number 1-Dark, 2-Exotic, 3-Happy, 4-Blues, 5-Spanish, 6-Dreamy, 7-Arpeggio : "))

if dict == 1:
    dict = dark_notes
if dict == 2:
    dict = exotic_notes
if dict == 3:
    dict = happy_notes
if dict == 4:
    dict = blues_notes
if dict == 5:
    dict = spanish_notes
if dict == 6:
    dict = dreamy_notes
if dict == 7:
    dict = arpeggio_notes

def change_volume(samples,volume_change):
    for sample in samples:
        numpy.multiply(sample, volume_change, out=sample, casting="unsafe")


'''This function generates a tone'''

def generate_saw_tone_from_string(note, sample_rate, seconds, volume):
    values = []
    frequency = 440.0 * 2.0 ** (dict[note] / 12.0)
    sample_length = int(seconds * 44100)
    for i in range(0, sample_length):
        value = math.sin(2 * math.pi * frequency * (i / sample_rate)) * \
                (volume * BIT_DEPTH)
        value_2 = 2 * (math.sin(frequency * (i / sample_rate)) *
                       (volume * BIT_DEPTH)) / -math.pi
        value_3 = 4 * (math.sin(frequency * (i / sample_rate)) *
                       (volume * BIT_DEPTH)) / math.pi
        for j in xrange(0, CHANNELS):
            values.append(value)
            #values.append(value_2)
            #values.append(value_3)

    return values

'''This makes a random list of various notes from the dictionary'''

random_music = []

# you can choose the number of notes that will be played
def generate_random_music(number_of_notes, dict):
    current_number_of_notes = 0
    while number_of_notes > current_number_of_notes:
        # creates a list called random_music out of the notes in the dictionary
        random_music.append(random.choice(dict.keys()))
        current_number_of_notes += 1
    print random_music


'''This function uses the tone generator to create the music samples '''

data_to_save = []
def write_melody(list_of_notes, tune_speed):
    for note in list_of_notes[:]:
        if tune_speed == 3:
            note_length = random.choice([0.2, 0.2, 0.4, 0.1, 0.1])
        if tune_speed == 2:
            note_length = random.choice([0.2, 0.4, 0.4, 1, 0.6, 0.8])
        if tune_speed == 1:
            note_length = random.choice([1.2, 1, 1.4, 1, 0.5])

        data_to_save.extend(generate_saw_tone_from_string
                            (note, SAMPLE_RATE, note_length, 1000.0))


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




note_speed = int(raw_input("Choose a speed 1-Slow, 2-Medium, 3-Fast: "))
tune_length = int(raw_input("Choose the length of the track (~30-200): "))
file_name = raw_input("Name your music file: ")

generate_random_music(tune_length, dict)

write_melody(random_music, note_speed)

save_melody(data_to_save, file_name +".wav")
