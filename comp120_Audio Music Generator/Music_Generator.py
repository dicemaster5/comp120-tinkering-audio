import numpy
import wave
import struct
import random

from Sound_Wave_Generators import *

'''
These function create, write and save the notes together all in one wav file for the user to listen to
'''

def change_volume(samples, volume_change):
    for sample in samples:
        numpy.multiply(sample, volume_change, out=sample, casting="unsafe")


'''This makes a random list of various notes from the dictionary'''

random_music = []


# you can choose the number of notes that will be played
def generate_random_music(number_of_notes, note_dict):
    current_number_of_notes = 0
    while number_of_notes > current_number_of_notes:
        # creates a list called random_music out of the notes in the dictionary
        random_music.append(random.choice(note_dict.keys()))
        current_number_of_notes += 1
    print random_music


'''This function uses the tone generator to create the music samples '''

data_to_save = []


def write_melody(list_of_notes, tune_speed, sound_wave_type, note_dict):
    for note in list_of_notes[:]:
        # this chooses how long each note in the song will be on average
        if tune_speed == 3:
            note_length = random.choice([0.2, 0.2, 0.4, 0.1, 0.1])
        if tune_speed == 2:
            note_length = random.choice([0.2, 0.4, 0.4, 1, 0.6, 0.8])
        if tune_speed == 1:
            note_length = random.choice([1.2, 1, 1.4, 1, 0.5])
        # this chooses the wave to generate for each note based on what the user selected
        if sound_wave_type == 1:
            data_to_save.extend(generate_sine_tone_from_string
                                (note, SAMPLE_RATE, note_length, 1000.0, note_dict))
        if sound_wave_type == 2:
            data_to_save.extend(generate_square_tone_from_string
                                (note, SAMPLE_RATE, note_length, 1500.0, note_dict))
        if sound_wave_type == 3:
            data_to_save.extend(generate_saw_tone_from_string
                                (note, SAMPLE_RATE, note_length, 1500.0, note_dict))


'''This function saves the data as a wav file in the same file directory as the main file'''


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
