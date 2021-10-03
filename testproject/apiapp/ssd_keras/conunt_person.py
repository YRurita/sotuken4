


def count_person():
    import cv2
    from camera import camera
    import keras
    from keras.applications.imagenet_utils import preprocess_input
    from keras.backend.tensorflow_backend import set_session
    from keras.models import Model
    from keras.preprocessing import image
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.misc import imread
    import tensorflow as tf

    from ssd import SSD300
    from ssd_utils import BBoxUtility


    voc_classes = ['Aeroplane', 'Bicycle', 'Bird', 'Boat', 'Bottle',
                'Bus', 'Car', 'Cat', 'Chair', 'Cow', 'Diningtable',
                'Dog', 'Horse','Motorbike', 'Person', 'Pottedplant',
                'Sheep', 'Sofa', 'Train', 'Tvmonitor']
    NUM_CLASSES = len(voc_classes) + 1


    input_shape=(300, 300, 3)
    model = SSD300(input_shape, num_classes=NUM_CLASSES)
    model.load_weights('weights_SSD300.hdf5', by_name=True)
    bbox_util = BBoxUtility(NUM_CLASSES)

    inputs = []
    images = []

    #写真撮影
    #camera()

    img_path = 'apiapp/static/pic_sub/photo.jpg'
    img = image.load_img(img_path, target_size=(300, 300))
    img = image.img_to_array(img)
    images.append(imread(img_path))
    inputs.append(img.copy())

    inputs = preprocess_input(np.array(inputs))




    preds = model.predict(inputs, batch_size=1, verbose=1)
    results = bbox_util.detection_out(preds)

    import matplotlib.pyplot as plt
    for i, img in enumerate(images):
        # Parse the outputs.
        det_label = results[i][:, 0]
        det_conf = results[i][:, 1]
        det_xmin = results[i][:, 2]
        det_ymin = results[i][:, 3]
        det_xmax = results[i][:, 4]
        det_ymax = results[i][:, 5]

        # Get detections with confidence higher than 0.6.
        top_indices = [i for i, conf in enumerate(det_conf) if conf >= 0.6]

        top_conf = det_conf[top_indices]
        top_label_indices = det_label[top_indices].tolist()
        top_xmin = det_xmin[top_indices]
        top_ymin = det_ymin[top_indices]
        top_xmax = det_xmax[top_indices]
        top_ymax = det_ymax[top_indices]

        colors = plt.cm.hsv(np.linspace(0, 1, 21)).tolist()

        plt.imshow(img / 255.)
        currentAxis = plt.gca()
        num = 0
        for i in range(top_conf.shape[0]):
            xmin = int(round(top_xmin[i] * img.shape[1]))
            ymin = int(round(top_ymin[i] * img.shape[0]))
            xmax = int(round(top_xmax[i] * img.shape[1]))
            ymax = int(round(top_ymax[i] * img.shape[0]))
            score = top_conf[i]
            label = int(top_label_indices[i])
            label_name = voc_classes[label - 1]
            #15が出力された数が写っている人数
            #print(label)
            if label == 15:
                num = num + 1
            #print(num)
            display_txt = '{:0.2f}, {}'.format(score, label_name)
            coords = (xmin, ymin), xmax-xmin+1, ymax-ymin+1
            color = colors[label]
            currentAxis.add_patch(plt.Rectangle(*coords, fill=False, edgecolor=color, linewidth=2))
            currentAxis.text(xmin, ymin, display_txt, bbox={'facecolor':color, 'alpha':0.5})

        f = open("apiapp/ssd_keras/num_list/num_list.txt", "w")
        f.write(str(num))
        f.close()        

        plt.subplots_adjust(left=0, right=1, bottom=0, top=1)   
        plt.savefig("apiapp/static/person.png")

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
        from apiapp.models import num_of_people

        objects = GridItem.objects.all()

        print(num)
        num_1 = num
        num_of_people.objects.all().delete()
        p = num_of_people.objects.create(num=num_1)
        
        #print("出来たよ")
        #plt.show()
        #人数を記述
        #print(num)

    #return num    