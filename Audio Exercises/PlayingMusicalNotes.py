import wave
import math
import struct

SAMPLE_WIDTH = 2
SAMPLE_RATE = 44100.0
BIT_DEPTH = 2.0
CHANNELS = 2

#notes = {"A":0,"A#":1,"B":2,"C":3,"C#":4,"D":5,"D#":6,"E":7,"F":8,"F#":9,"G":10,"G#":11}

# note_frequency = 440.0 * 2.0 ** (note_number / 12)

def generate_sine_wave(note,sample_rate, sample_length, volume):
    notes = {"A": 0, "A#": 1, "B": 2, "C": 3, "C#": 4, "D": 5, "D#": 6, "E": 7, "F": 8, "F#": 9, "G": 10, "G#": 11}
    values = []
    frequency = 440.0 * 2.0 ** (notes[note] / 12.0)
    for i in range(0, sample_length):
        value = math.sin(2 * math.pi * frequency * (i / sample_rate)) * (volume * BIT_DEPTH)
        for j in xrange(0, CHANNELS):
            values.append(value)

    return values


def save_wave_file(filename, wav_data, sample_rate):
    packed_values=[]
    for i in range(0,len(wav_data)):
        packed_value = struct.pack('h', wav_data[i])
        packed_values.append(packed_value)

    noise_out = wave.open(filename, 'w')
    noise_out.setparams((CHANNELS, SAMPLE_WIDTH, sample_rate, 0, 'NONE', 'not compressed'))
    value_str = ''.join((str(n) for n in packed_values))
    noise_out.writeframes(value_str)
    noise_out.close()


tone_values_one = generate_sine_wave('A#', SAMPLE_RATE, 132000, 1000.0)
save_wave_file('Tone2.wav',tone_values_one,SAMPLE_RATE)