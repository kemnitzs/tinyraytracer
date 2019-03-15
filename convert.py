#!/usr/bin/python2
from PIL import Image

im = Image.open("out.ppm")
im.save("raytracer_result.jpg")
