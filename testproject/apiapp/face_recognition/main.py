import face_recognition
import cv2
import numpy as np
from camera import camera

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
def main():
    camera()
    video_capture = cv2.imread("apiapp/static/pic_sub/photo.jpg")

    """
    # Load a sample picture and learn how to recognize it.
    matumoto_image = face_recognition.load_image_file("apiapp/static/pic_sample/matumoto.jpg")
    matumoto_face_encoding = face_recognition.face_encodings(matumoto_image)[0]

    # Load a second sample picture and learn how to recognize it.
    aiba_image = face_recognition.load_image_file("apiapp/static/pic_sample/aiba.jpg")
    aiba_face_encoding = face_recognition.face_encodings(aiba_image)[0]

    # Load a second sample picture and learn how to recognize it.
    oono_image = face_recognition.load_image_file("apiapp/static/pic_sample/oono.jpg")
    oono_face_encoding = face_recognition.face_encodings(oono_image)[0]

    # Load a second sample picture and learn how to recognize it.
    nino_image = face_recognition.load_image_file("apiapp/static/pic_sample/nino.jpg")
    nino_face_encoding = face_recognition.face_encodings(nino_image)[0]

    # Load a second sample picture and learn how to recognize it.
    sakurai_image = face_recognition.load_image_file("apiapp/static/pic_sample/sakurai.jpg")
    sakurai_face_encoding = face_recognition.face_encodings(sakurai_image)[0]
    
    # Create arrays of known face encodings and their names
    
    known_face_encodings = [
        matumoto_face_encoding,
        aiba_face_encoding,
        oono_face_encoding,
        nino_face_encoding,
        sakurai_face_encoding
    ]
    known_face_names = [
        "matumoto",
        "aiba",
        "oono",
        "nino",
        "sakurai"
    ]
    """
    
    import django
    import os
    import sys
    import pprint
    import time

    

    path_face = os.getcwd()
    print(path_face)
    #sys.path.append(path_face + "\\apiapp")
    #sys.path.append("C:\\卒研13_api\\testproject\\apiapp\\")
    #sys.path.append("C:\\卒研13_api\\testproject\\testproject\\")
    sys.path.append(path_face)
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testproject.settings')
    django.setup()

    from apiapp.models import GridItem
    from apiapp.models import person_in_the_room

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
        globals()[dynamicvariable_name_1] = face_recognition.load_image_file(obj.picture)
        globals()[dynamicvariable_name_2] = face_recognition.face_encodings(globals()[dynamicvariable_name_1])[0]


        known_face_encodings.append(globals()[dynamicvariable_name_2])
        known_face_names.append(obj.name)



    frame = video_capture
    
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame, model="hog") #, model="cnn"をrgb_rameの後に追加すると高精度になるが、gpuでの計算になり時間がかかる。gpuがない場合は、model="hog"
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    name_array = []

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            name_array.append(name)

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (0, 0, 0), 1)

    # write the resulting image
    f = open("apiapp/face_recognition/name_list/name_list.txt", "w")
    names = ",".join(name_array)
    f.write(names)
    f.close()

    
    print(len(name_array))
    person_in_the_room.objects.all().delete()
    for item in name_array:
        box = GridItem.objects.get(name=item)
        print(box.name)
        print(box.number)
        p = person_in_the_room.objects.create(number=box.number,name=box.name)

    #cv2.imwrite('apiapp/face_recognition/pic_result/face.jpg', frame)
    cv2.imwrite('apiapp/static/face.jpg', frame)


# Hit 'q' on the keyboard to quit!
#if cv2.waitKey(1) & 0xFF == ord('q'):


# Release handle to the webcam
#video_capture.release()
#cv2.destroyAllWindows()