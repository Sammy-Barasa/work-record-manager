from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from workrecords.models import Work
from django.contrib.auth import get_user_model
from workrecords.serializers import UpdateWorkSerializer, WorkSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
# Create your views here.




# class WorkDetailView(generics.GenericAPIView):
#     serializer_class = WorkSerializer
#     # overriding get queryset

#     def get_queryset(self):
#         """
#         returns specific work detail 
#         """
#         id = self.kwargs['work_id']
#         return Work.objects.get(id=id)

#     def get(self, request, work_id):
#         try:
#             serializer = self.serializer_class(self.get_queryset())
#             message = f"work {work_id} detail"
#             return Response({"message": message, "data": serializer.data}, status=status.HTTP_200_OK)
#         except serializer.errors as error:
#             return Response({"message": error, "data": serializer.data}, status=status.HTTP_404_OK)
class GetWorkView(generics.GenericAPIView):
    permission_classes =(IsAuthenticated,)
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    
    
    def get(self,request,**kwargs):
        serializer= self.serializer_class(self.get_queryset(),many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UpdateWorkView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateWorkSerializer
    lookup_field = "work_id"

    # overriding get queryset

    def get_queryset(self):
        """
        returns specific work for detail(get),updated(patch),deleting(delete) 
        """
        id = self.kwargs['work_id']
        print(id)
        queryset = Work.objects.get(id=id)
        return queryset

    # get work detail
    def get(self, request, work_id):
        try:
            serializer = self.serializer_class(self.get_queryset())
            message = f"work {work_id} detail"
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as error:
            return Response(data={"detail": error}, status=status.HTTP_404_OK)

    # update work
    def put(self, request, work_id):
        print(work_id)
        data = request.data
        serializer = self.serializer_class(self.get_queryset(),data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(data={"message": "work has been updated"}, status=status.HTTP_200_OK)

    # delete work 
    def delete(self, request, work_id):
        work=self.get_queryset()
        operation=work.delete()
        if operation:
            message = f"work {work_id} has been deleted"
            return Response({"message": message}, status=status.HTTP_200_OK)
        return Response(data={"message": message}, status=status.HTTP_400_BAD_REQUEST)


# get personal person options
# get personal worktype options
# 
