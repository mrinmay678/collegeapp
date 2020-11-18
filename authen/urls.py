from django.urls import path,include
from rest_framework import routers
from .views import TeacherViewSet,StudentViewSet,UserViewSet


urlpatterns = [
    #path('', include(router.urls)),
    path('user/', UserViewSet.as_view()),
    path('teacher/',TeacherViewSet),
    path('student/',StudentViewSet)

]
