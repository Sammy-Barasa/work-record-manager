from django.urls.conf import path
from workrecords.views import  UpdateWorkView, GetWorkView,GetWorkOptionsView, TestGSM

urlpatterns = [
    path("<int:work_id>/", UpdateWorkView.as_view(),
         name="work_rud_endpoint"),
    path("", GetWorkView.as_view(),
         name="work_endpoint"),
    path("options/", GetWorkOptionsView.as_view(),
         name="work_options_endpoint"),
    path("gsm/", TestGSM.as_view(),
         name="test_gsm_endpoint"),
]
