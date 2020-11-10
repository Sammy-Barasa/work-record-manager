from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from workrecords.models import Work
from django.contrib.auth import get_user_model
from workrecords.serializers import UpdateWorkSerializer
from django.core.exceptions import ObjectDoesNotExist
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
        


class UpdateWorkView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateWorkSerializer
    queryset = Work.objects.all()
    lookup_field = "id"

    # overriding get queryset

    def get_queryset(self):
        """
        returns specific work for detail(get),updated(patch),deleting(delete) 
        """
        id = self.kwargs['work_id']
        print(id)
        return Work.objects.filter(id=id)

    # get work detail
    def get(self, request, work_id):
        try:
            serializer = self.serializer_class(self.get_queryset())
            message = f"work {work_id} detail"
            return Response({"message": message, "data": serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as error:
            return Response({"message": error, "data": serializer.data}, status=status.HTTP_404_OK)

    # update work
    def patch(self, request, work_id):
        data = request.data
        serializer = self.serializer_class(self.get_queryset(),data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response({"message": "work has been updated"}, status=status.HTTP_200_OK)

    # delete work 
    def delete(self, request, work_id):
        work=self.get_queryset()
        operation=work.delete()
        if operation:
            message = f"work {work_id} has been deleted"
            return Response({"messages": message}, status=status.HTTP_200_OK)
        return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)


# get personal person options
# get personal worktype options
# 
