from Dictionaries_Of_Notes import *

'''
This is the code that manages the user interface so the 
User can create and customize their own randomised music
'''

# user picks a genre
note_dict = int(
    raw_input("Pick a genre number 1-Dark, 2-Exotic, 3-Happy, 4-Blues, 5-Spanish, 6-Dreamy, 7-Arpeggio, 8-Random : "))
# user picks a type of tone to generate
wave_type = int(raw_input("Choose a sound wave type, 1-Sine, 2-Square, 3-Sawtooth : "))

# this assigns the different dictionaries to integers that the user can choose from
if note_dict == 1:
    note_dict = dark_notes
if note_dict == 2:
    note_dict = exotic_notes
if note_dict == 3:
    note_dict = happy_notes
if note_dict == 4:
    note_dict = blues_notes
if note_dict == 5:
    note_dict = spanish_notes
if note_dict == 6:
    note_dict = dreamy_notes
if note_dict == 7:
    note_dict = arpeggio_notes
if note_dict == 8:
    note_dict = random_notes

# the user picks the speed of the music based on the length of each note played
note_speed = int(raw_input("Choose a speed 1-Slow, 2-Medium, 3-Fast: "))

# the user picks how many notes are created in the entire track, this changes
# the length of the track and is roughly proportional to the previously
# chosen note_length (fast requires a higher tune_length)
tune_length = int(raw_input("Choose the length of the track (~30-200): "))

# the user specifies the file name that is created
file_name = raw_input("Name your music file: ")
