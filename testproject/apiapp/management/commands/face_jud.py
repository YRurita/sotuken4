from django.core.management.base import BaseCommand
import os
import sys
import pprint
import time

path_face = os.getcwd()
sys.path.append(path_face + "\\apiapp\\face_recognition")
sys.path.append(path_face + "\\apiapp\\ssd_keras")

from main import main
from main2 import main2

class Command(BaseCommand):
    def handle(self, *args, **options):
        num = 0
        try:
            while True:
                num = num + 1
                print("実行回数は" + str(num) + "回です")
                main()
                main2()
                time.sleep(60)
        except KeyboardInterrupt:
            print('!!FINISH!!')