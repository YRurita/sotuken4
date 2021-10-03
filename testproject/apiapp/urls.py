from rest_framework import routers
from .views import GridItemViewSet, person_in_the_roomViewSet, num_of_peopleViewSet
router = routers.DefaultRouter()
#rを文字列の前に付与してエスケープシーケンスを無効化し、そのままの文字として扱う
router.register(r'griditem', GridItemViewSet)
router.register(r'person_in_the_room', person_in_the_roomViewSet)
router.register(r'num_of_people', num_of_peopleViewSet)