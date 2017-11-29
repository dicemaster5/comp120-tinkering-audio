'''
All the notes and note styles used to create different types of music genres
'''

# dictionary for the various notes, spans three octaves

random_notes = {"iA": -12, "iA#": -11, "iB": -10, "iC": -9, "iC#": -8, "iD": -7,
                "iD#": -6, "iE": -5, "iF": -4, "iF#": -3, "iG": -2, "iG#": -1, "A": 0,
                "A#": 1, "B": 2, "C": 3, "C#": 4, "D": 5, "D#": 6, "E": 7,
                "F": 8, "F#": 9, "G": 10, "G#": 11, "a": 12, "a#": 13, "b": 14,
                "c": 15, "c#": 16, "d": 17, "d#": 18, "e": 19, "f": 20, "f#": 21,
                "g": 22, "g#": 23}

# this assigns the different scales to dictionaries
dark_notes = {"iC": -9, "iC#": -8, "iD#": -6, "iF": -4, "iF#": -3, "iG#": -1, "A#": 1}  # mysterious jazzy

exotic_notes = {"C": 3, "C#": 4, "E": 7, "F": 8, "G": 10, "G#": 11, "a#": 13}  # exotic, middle eastern

happy_notes = {"C": 3, "D": 5, "E": 7, "a": 12, "b": 14, "F": 8, "B": 2, "G": 10}  # major scale

blues_notes = {"iA": -12, "iA#": -11, "iB": -10, "iD": -7, "iE": -5, "iF": -4, "A": 0}  # blues

spanish_notes = {"C": 3, "C#": 4, "D#": 6, "F": 8, "G": 10, "G#": 11, "a#": 13}  # spanish/flamenco

dreamy_notes = {"C": 3, "D": 5, "E": 7, "F#": 9, "G#": 11, "a#": 13}  # dreamy/underwater

arpeggio_notes = {"iA": -12, "iC#": -8, "iE": -5, "iG#": -1, "A": 0, }  # Arpeggio

pre_written_melody = ['D', 'F', 'd', 'D', 'F', 'd', 'e', 'f', 'e', 'f',
                      'e', 'c', 'A', 'A', 'D', 'F', 'G', 'A', 'A', 'D',
                      'F', 'G', 'E']
