from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from workrecords.models import Work, PersonChoises
from django.contrib.auth import get_user_model
from workrecords.serializers import WorkSerializer, WorkCreateSerializer
from Users.serializers import PersonSerializer, PersonUpdateSerializer, PersonCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from Users.utils import StatisticThread, getStats
# Create your views here.

# create ,get work API viw
class UserWorksView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
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
            return queryset.filter(assigned_to=user).order_by('-last_modified')
    
    def get(self,request,user_id):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        scope={'hasNoList':False}
        if len(serializer.data)==0:
            scope['hasNoList']=True
            stats={'total':0,'paid_total':0,'not_paid_total':0}
        stats=getStats.calculate_stats(serializer.data)
        return Response(data={'data':serializer.data,'scope':scope,'stats':stats}, status=status.HTTP_200_OK)


class UserCreateWorksView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkCreateSerializer


    # create work for user
    def post(self, request,user_id):
        data = request.data
        print(request.user)
        serializer = self.serializer_class(data=data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(
                created_by=request.user, assigned_to=request.user)
            print(serializer.data)
            return Response(data={"message": "work has been added"}, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            print(error)
            print(serializer.errors)
            return Response(data={"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            
class UserPersonView(generics.GenericAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = PersonSerializer

    # overriding get queryset

    def get_queryset(self):
        """
        returns person for User

        """
        queryset = PersonChoises.objects.all()
        return queryset

    # get person detail
    def get(self, request, user_id):
        scope = {'hasNoList': False}
        try:
            serializer = self.serializer_class(self.get_queryset().filter(user=request.user),many=True)
            
            if len(serializer.data) == 0:
                scope['hasNoList'] = True
            return Response(data={'data': serializer.data, 'scope': scope}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as error:
            return Response(data={"detail": error}, status=status.HTTP_404_OK)
        
        
class UserCreatePersonView(generics.GenericAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = PersonCreateSerializer
    # add person

    def post(self, request, user_id):
        data = request.data
        serializer = self.serializer_class(
            data=data, context={'request': request,'userId':user_id})
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(user=request.user)
            print(serializer.data)
            return Response(data={"message": "person has been created"}, status=status.HTTP_200_OK)
        except ValidationError as error:
            return Response(data={"message": error}, status=status.HTTP_400_BAD_REQUEST)

class UserUpdatePersonView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PersonUpdateSerializer
    lookup_field = "personchoices_id"

    # overriding get queryset

    def get_queryset(self):
        """
        returns specific person for detail(get),updated(put),deleting(delete) 
        """
        id = self.kwargs['personchoices_id']
        print(id)
        queryset = PersonChoises.objects.get(id=id)
        return queryset

    # get person detail
    def get(self, request, user_id,personchoices_id):
        try:
            serializer = self.serializer_class(self.get_queryset())
            message = f"person {personchoices_id} detail"
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as error:
            return Response(data={"detail": error}, status=status.HTTP_404_OK)


    # update person
    def put(self, request, user_id,personchoices_id):
        print(personchoices_id)
        data = request.data
        serializer = self.serializer_class(self.get_queryset(), data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(data={"message": "person has been updated"}, status=status.HTTP_200_OK)

    # delete person
    def delete(self, request, user_id,personchoices_id):
        person = self.get_queryset()
        operation = person.delete()
        if operation:
            message = f"work {personchoices_id} has been deleted"
            return Response({"message": message}, status=status.HTTP_200_OK)
        return Response(data={"message": message}, status=status.HTTP_400_BAD_REQUEST)
