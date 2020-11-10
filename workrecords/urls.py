from django.urls.conf import path
from workrecords.views import  UpdateWorkView

urlpatterns = [
    path("<int:work_id>/", UpdateWorkView.as_view(),
         name="work_rud_endpoint"),
    
]
