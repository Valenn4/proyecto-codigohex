from django.urls import path
from api.views import ActivityByUserView, ActivityByUserDateView

urlpatterns = [
    path("activities/<int:id>", ActivityByUserView.as_view({'get': 'list', 'post':'create'})),
    path("activities/<int:id>/<int:year>/<int:month>/<int:day>", ActivityByUserDateView.as_view({'get': 'list'}))
]