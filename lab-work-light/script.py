import numpy as np
import matplotlib.pyplot as plt
import imageio
from cycler import cycler

import lightFunctions

from time import sleep
from picamera import PiCamera

try:
    file_name = input() + '.jpg'
    camera = PiCamera()
    camera.resolution = (1920, 1080)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(file_name)
    lightFunctions.readIntensity(file_name, 'test_plot.jpg', 'both', 'white')
finally:
    print("Ono rabotaet (ili net)")