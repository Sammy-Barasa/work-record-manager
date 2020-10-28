from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from workrecords.models import Work
from django.contrib.auth import get_user_model
from workrecords.serializers import WorkSerializer, UpdateWorkSerializer
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
            return queryset.filter(user=user).order_by('date')
    
    def get(self,request,user_id):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response({"message":"get method working","data":serializer.data}, status=status.HTTP_200_OK)


    # create work for user
    def post(self, request,user_id):
        data = request.data
        print(request.user)
        serializer = self.serializer_class(data=data,context={'user_id': user_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response({"message": "work has been added"}, status=status.HTTP_201_CREATED)


class WorkDetailView(generics.GenericAPIView):
    serializer_class = WorkSerializer
    # overriding get queryset

    def get_queryset(self):
        """
        returns specific work detail 
        """
        id = self.kwargs['work_id']
        return Work.objects.get(id=id)

    def get(self, request, work_id):
        serializer = self.serializer_class(self.get_queryset())
        message = f"work {work_id} detail"
        return Response({"message": message, "data": serializer.data}, status=status.HTTP_200_OK)


class UpdateWorkView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateWorkSerializer
    queryset = Work.objects.all()
    lookup_field = "id"

    # overriding get queryset

    def get_queryset(self):
        """
        returns specific work to be updated 
        """
        id = self.kwargs['id']
        print(id)
        return Work.objects.filter(id=id)

    # update work
    def patch(self, request, id):
        data = request.data
        serializer = self.serializer_class(self.get_queryset(),data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response({"message": "work has been updated"}, status=status.HTTP_200_OK)

    # delete work 
    def delete(self, request, id):
        work=self.get_queryset()
        operation=work.delete()
        if operation:
            message = f"work {id} has been deleted"
            return Response({"message": message}, status=status.HTTP_200_OK)
        return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)


# get personal person options
# get personal worktype options
# 
