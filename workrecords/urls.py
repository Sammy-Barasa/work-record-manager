from django.urls.conf import path
from workrecords.views import UserWorksView

urlpatterns = [
    path("user/<int:user_id>/", UserWorksView.as_view(), name="get_user_works_endpoint"),
]
