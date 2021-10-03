import django
import os
import sys
import pprint
import time
import face_recognition
import cv2
import numpy as np
from camera import camera

path_face = os.getcwd()
print(path_face)
#sys.path.append(path_face + "\\apiapp")
#sys.path.append("C:\\卒研13_api\\testproject\\apiapp\\")
#sys.path.append("C:\\卒研13_api\\testproject\\testproject\\")
sys.path.append(path_face)
pprint.pprint(sys.path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testproject.settings')
django.setup()

from apiapp.models import GridItem

objects = GridItem.objects.all()


known_face_encodings = []
known_face_names = []

for obj in objects:
    """
    print(obj.number)
    print(obj.name)
    print(obj.picture)
    """
    dynamicvariable_name_1 = obj.name + "_image"
    dynamicvariable_name_2 = obj.name + "_face_encoding"
    locals()[dynamicvariable_name_1] = face_recognition.load_image_file(obj.picture)
    locals()[dynamicvariable_name_2] = face_recognition.face_encodings(locals()[dynamicvariable_name_1])[0]
    known_face_encodings.append(obj.name + "_face_encoding")
    known_face_names.append(obj.name)


print(known_face_encodings,known_face_names)