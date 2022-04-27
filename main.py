#!/usr/bin/python3
import pathlib
import pygubu

import drowsiness_detection

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "wykrywanie-sennosci.ui"



class WykrywanieSennosciApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("main_frame", master)

        self.__tkvar = None
        builder.import_variables(self, ["__tkvar"])

        builder.connect_callbacks(self)
        self.sound_path = PROJECT_PATH / "sounds" / "alarm.wav"


    def run(self):
        self.mainwindow.mainloop()

    def start_program(self):
        drowsiness_detection.run(self.sound_path)

    def set_sound(self, option):
        base_sound_path = PROJECT_PATH / "sounds"
        if option == "Alarm":
            self.sound_path = base_sound_path / "alarm.wav"
        elif option == "DoubleBeep":
            self.sound_path = base_sound_path / "double-beep.wav"
        elif option == "DoorBell":
            self.sound_path = base_sound_path / "doorbell.wav"
        elif option == "SciFi":
            self.sound_path = base_sound_path / "sci-fi.wav"
        elif option == "Tone-Loop":
            self.sound_path = base_sound_path / "simple-tone-loop.wav"


if __name__ == "__main__":
    app = WykrywanieSennosciApp()
    app.run()

