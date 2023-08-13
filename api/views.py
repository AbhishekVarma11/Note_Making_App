from django.shortcuts import render
from .models import Note

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer

@api_view(['GET'])
def getRoutes(request):
    return Response('This is using the Django Rest framework')


@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all()
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):
    notes=Note.objects.get(id=pk)
    serializer=NoteSerializer(notes,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data=request.data
    note=Note.objects.create(body=data['body'])
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
    data=request.data
    note=Note.objects.get(id=pk)
    serializer=NoteSerializer(instance=note,data=data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')


