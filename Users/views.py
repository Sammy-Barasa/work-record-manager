from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from workrecords.models import Work
from django.contrib.auth import get_user_model
from workrecords.serializers import WorkSerializer
# Create your views here.

# create ,get work API viw
class UserWorksView(generics.GenericAPIView):
    serializer_class= WorkSerializer

    # overriding get queryset
    def get_queryset(self):
        """
        returns works for the specific user
        """
        queryset = Work.objects.all()
        id = self.kwargs['user_id']
        user = get_user_model().objects.get(pk=id)
        if user is not None:
            return queryset.filter(user=user).order_by('-date')
    
    def get(self,request,user_id):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    # create work for user
    def post(self, request,user_id):
        data = request.data
        print(request.user)
        serializer = self.serializer_class(data=data,context={'user_id': user_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(data={"message": "work has been added"}, status=status.HTTP_201_CREATED)