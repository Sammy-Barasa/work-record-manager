from django.urls.conf import path
from workrecords.views import  UpdateWorkView, GetWorkView,GetWorkOptionsView

urlpatterns = [
    path("<int:work_id>/", UpdateWorkView.as_view(),
         name="work_rud_endpoint"),
    path("", GetWorkView.as_view(),
         name="work_endpoint"),
    path("options/", GetWorkOptionsView.as_view(),
         name="work_options_endpoint"),
    
]
