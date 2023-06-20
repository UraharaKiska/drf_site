from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict

from creature.models import Creature, Category
from .permissions import *
from .serializers import CreatureSerializer


# class CreatureAPIView(generics.ListAPIView):
#     queryset = Creature.objects.all()
#     serializer_class = CreatureSerializer
#
#




class CreatureAPIList(generics.ListCreateAPIView):
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CreatureAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CreatureAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CreatureViewSet(viewsets.ModelViewSet):

    serializer_class = CreatureSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Creature.objects.all()[:3]

        return Creature.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})


# class CreatureAPIList(generics.ListCreateAPIView):
#     queryset = Creature.objects.all()
#     serializer_class = CreatureSerializer
#
# class CreatureAPIUpdate(generics.UpdateAPIView):
#     queryset = Creature.objects.all()
#     serializer_class = CreatureSerializer
#
# class CreatureAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Creature.objects.all()
#     serializer_class = CreatureSerializer

# class CreatureAPIView(APIView):
#     def get(self, request):
#         c = Creature.objects.all()
#         return Response({'posts': CreatureSerializer(c, many=True).data})
#
#     def post(self, request):
#         serializer = CreatureSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Creature.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = CreatureSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Creature.objects.get(pk=pk)
#             instance.delete()
#             instance.save()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"deleted": 'hui'})