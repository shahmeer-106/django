from rest_framework import viewsets
from .models import Student
from .serializer import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = TodoSerializer
