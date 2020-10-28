from django.urls.conf import path
from workrecords.views import UserWorksView, UpdateWorkView, WorkDetailView

urlpatterns = [
    path("user/<int:user_id>/", UserWorksView.as_view(), name="get_user_works_endpoint"),
    path("<int:work_id>/", WorkDetailView.as_view(),
         name="work_detail_endpoint"),
    path("<int:id>/update/", UpdateWorkView.as_view(),
         name="update_work_endpoint"),
]
