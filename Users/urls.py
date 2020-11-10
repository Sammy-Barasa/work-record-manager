from django.urls.conf import path
from Users.views import UserWorksView

urlpatterns = [
    path("<int:user_id>/", UserWorksView.as_view(),
         name="get_user_works_endpoint"),
]