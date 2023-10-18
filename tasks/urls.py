from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet,SearchViewSet

router = DefaultRouter()
router.register(r'', TasksViewSet)

urlpatterns = [
    path('search/<str:q>',SearchViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
