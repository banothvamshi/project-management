from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet

# Main router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'comments', CommentViewSet, basename='comments')

# Nested routers
projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'tasks', TaskViewSet, basename='project-tasks')

tasks_router = routers.NestedSimpleRouter(projects_router, r'tasks', lookup='task')
tasks_router.register(r'comments', CommentViewSet, basename='task-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(tasks_router.urls)),
]