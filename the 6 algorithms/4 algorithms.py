import pygame
import wave
import numpy
import math
import struct

pygame.init()
pygame.mixer.init()

SAMPLE_WIDTH = 2
SAMPLE_RATE = 44100.0
BIT_DEPTH = 2.0
CHANNELS = 2

def change_volume(samples,volume_change):
    for sample in samples:
        numpy.multiply(sample, volume_change, out=sample, casting="unsafe")

def generate_tone_from_string(note,sample_rate, sample_length, volume):
    notes = {"A": 0, "A#": 1, "B": 2, "C": 3, "C#": 4, "D": 5, "D#": 6, "E": 7, "F": 8, "F#": 9, "G": 10, "G#": 11}
    values = []
    frequency = 440.0 * 2.0 ** (notes[note] / 12.0)
    for i in range(0, sample_length):
        value = math.sin(2 * math.pi * frequency * (i / sample_rate)) * (volume * BIT_DEPTH)
        for j in xrange(0, CHANNELS):
            values.append(value)

    return values


def create_melody_from_tones(list_of_tones):
    for i in list_of_tones:
        for value in i:

            list_of_tones[0].append(i)


def save_melody(wav_data, name_of_file):
    packed_values=[]
    for i in range(0,len(wav_data)):
        packed_value = struct.pack('h', wav_data[i])
        packed_values.append(packed_value)

    noise_out = wave.open(name_of_file, 'w')
    noise_out.setparams((CHANNELS, SAMPLE_WIDTH, SAMPLE_RATE, 0, 'NONE', 'not compressed'))
    value_str = ''.join((str(n) for n in packed_values))
    noise_out.writeframes(value_str)
    noise_out.close()


note1 = generate_tone_from_string('A#', SAMPLE_RATE, 132000, 1000.0)
note2 = generate_tone_from_string('D', SAMPLE_RATE, 132000, 1000.0)
note3 = generate_tone_from_string('A', SAMPLE_RATE, 132000, 1000.0)
note4 = generate_tone_from_string('f#', SAMPLE_RATE, 132000, 1000.0)

melody_list = [note1, note2, note3, note4]
new_melody = note1.extend(note2)
save_melody(note1, "newMelody.wav")
