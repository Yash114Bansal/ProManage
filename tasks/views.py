from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import TasksSerializer, subTasksSerializer
from .models import Tasks
from .permissions import IsSuperuserOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector

class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly,IsAuthenticated]

    def get_queryset(self):

        if(self.request.method not in ["GET","PATCH","PUT"] or self.request.user.is_staff):
            return Tasks.objects.all()
        
            
        return Tasks.objects.filter(user=self.request.user)

class SearchViewSet(ReadOnlyModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    def get_queryset(self):
        query = self.kwargs.get('q')
        print(query)
        search_vector = SearchVector('title','description')

        return Tasks.objects.annotate(search=search_vector).filter(search__icontains=query).filter(user=self.request.user)
