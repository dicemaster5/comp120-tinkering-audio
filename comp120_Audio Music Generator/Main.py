from User_Interface_Manager import *
from Music_Generator import *

'''
This is the Main file of the application, it calls everything else from here.
Running this file will run the application and allow you to generate and customize random music
thanks to the UI down in the console.

The application will first ask you to input a number from 1-8 to choose a certain genre for the music
then it will ask you to input a number from 1-3 for the type of sound wave it will use
then it will ask you to input a number from 1-3 for the speed of the music
then it will ask you to input a number from 30-200 for the length of the music track
it will then ask you to input the name you want the file to be saved as
the saved music file will be saved the in the same file directory as the main file.
'''

generate_random_music(tune_length, note_dict)

write_melody(random_music, note_speed, wave_type, note_dict)

save_melody(data_to_save, file_name + ".wav")
