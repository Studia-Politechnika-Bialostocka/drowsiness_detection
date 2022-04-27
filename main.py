#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
import pygubu
# from __future__ import print_function
from PIL import Image
from PIL import ImageTk
# import Tkinter as tki
import threading
import datetime
import numpy as np
import imutils
import cv2
import os

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

    def run(self):
        self.mainwindow.mainloop()

    def start_program(self):
        # get path to sound file from sounds directory
        # self.SOUND_PATH = os.path.join(PROJECT_PATH, "sounds", self.__tkvar.get())
        sound_path = "C:\\Users\\Mateusz\\Documents\\university\\drowsiness_detection\\sounds\\doorbell.wav"
        print("Start programu")
        video_frame = self.builder.get_object("video_frame")
        drowsiness_detection.run(video_frame, sound_path)

    def set_sound(self, option):
        pass


if __name__ == "__main__":
    app = WykrywanieSennosciApp()
    app.run()

