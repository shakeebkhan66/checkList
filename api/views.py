from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.models import MyCheckList, MyCheckListItem
from api.serializers import ChecklistSerializer, ChecklistItemsSerializer
from rest_framework.serializers import Serializer
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated


# Create your views here.
# @api_view()
# def show_Hello(request):
#     return HttpResponse({'name': 'Shakeeb Ahmed Khan'})


# GETTING ALL DATA
class Checklist(APIView):
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = MyCheckList.objects.all()
        serializer = self.serializer_class(data, many=True)
        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GETTING DATA BY PASSING ID
class CheckListWithId(APIView):
    serializer_class = ChecklistSerializer

    # SIMPLE WAY TO GET BY ID BUT NOT HANDLING EXCEPTIONS
    # def get(self, request, pk, format=None):
    #     serializer = self.serializer_class(MyCheckList.objects.get(pk=pk))
    #     serialized_data = serializer.data
    #     return Response(serialized_data)

    # A GOOD WAY TO HANDLE EXCEPTIONS ERROR

    # THIS FUNCTION WORKS TO RAISE EXCEPTION IN CASE OF NOT FINDING THE SEARCH ID
    def get_object(self, pk):
        try:
            return MyCheckList.objects.get(pk=pk)
        except MyCheckList.DoesNotExist:
            raise Http404

    def get(self, request, pk, fomat=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChecklistCreateApi(APIView):
    serializer_class = ChecklistItemsSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChecklistItemApi(APIView):
    serializer_class = ChecklistItemsSerializer

    # THIS FUNCTION WORKS TO RAISE EXCEPTION IN CASE OF NOT FINDING THE SEARCH ID
    def get_object(self, pk):
        try:
            return MyCheckListItem.objects.get(pk=pk)
        except MyCheckListItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, fomat=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist_item = self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



