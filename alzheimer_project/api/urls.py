from django.urls import path
from api.views import ActivityByUserView, ActivityByUserDateView
#from api.views import ActivityByUserView, ActivityByUserDateView, ObjectView, ActionView, GameView, MusicView

urlpatterns = [
    path("activities/<int:id>", ActivityByUserView.as_view({'get': 'list', 'post':'create'})),
    path("activities/<int:id>/<int:year>/<int:month>/<int:day>", ActivityByUserDateView.as_view({'get': 'list'}))
    
]

'''
    path("activities/object/", ObjectView.as_view({'post':'create'})),
    path("activities/action/", ActionView.as_view({'post':'create'})),
    path("activities/game/", GameView.as_view({'post':'create'})),
    path("activities/music/", MusicView.as_view({'post':'create'}))
    '''