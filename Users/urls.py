from django.urls.conf import path
from Users.views import UserWorksView, UserCreateWorksView, UserPersonView, UserUpdatePersonView

urlpatterns = [
    path("<int:user_id>/", UserWorksView.as_view(),
         name="get_user_works_endpoint"),
    path("<int:user_id>/create/", UserCreateWorksView.as_view(),
         name="create_user_works_endpoint"),
    path("<int:user_id>/person/", UserPersonView.as_view(),
         name="user_persons_endpoint"),
    path("<int:user_id>/person/<int:personchoices_id>/", UserUpdatePersonView.as_view(),
         name="update_user_persons_endpoint"),
]
