import math

'''
The different sound wave generators used to create different sounding notes
'''

# basic parameters for the tone generators
SAMPLE_WIDTH = 2
SAMPLE_RATE = 44100.0
BIT_DEPTH = 2.0
CHANNELS = 2

'''This function generates a sine wave tone'''


def generate_sine_tone_from_string(note, sample_rate, seconds, volume, dict):
    values = []
    frequency = 440.0 * 2.0 ** (dict[note] / 12.0)
    sample_length = int(seconds * 44100)
    for i in range(0, sample_length):
        value = math.sin(2 * math.pi * frequency * (i / sample_rate)) * \
                (volume * BIT_DEPTH)
        for j in xrange(0, CHANNELS):
            values.append(value)

    return values


'''This function generates a square wave tone'''


def generate_square_tone_from_string(note, sample_rate, seconds, volume, dict):
    values = []
    frequency = 440.0 * 2.0 ** (dict[note] / 12.0)
    sample_length = int(seconds * 44100)
    for i in range(0, sample_length):
        value = 2 * (math.sin(frequency * (i / sample_rate)) *
                     (volume * BIT_DEPTH)) / -math.pi
        for j in xrange(0, CHANNELS):
            values.append(value)

    return values


'''This function generates a sawtooth wave tone'''


def generate_saw_tone_from_string(note, sample_rate, seconds, volume, dict):
    values = []
    frequency = 440.0 * 2.0 ** (dict[note] / 12.0)
    sample_length = int(seconds * 44100)
    for i in range(0, sample_length):
        value = 4 * (math.sin(frequency * (i / sample_rate)) *
                     (volume * BIT_DEPTH)) / math.pi
        for j in xrange(0, CHANNELS):
            values.append(value)

    return values
