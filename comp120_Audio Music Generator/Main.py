from User_Interface_Manager import *
from Music_Generator import *

generate_random_music(tune_length, note_dict)

write_melody(random_music, note_speed, wave_type, note_dict)

save_melody(data_to_save, file_name + ".wav")
