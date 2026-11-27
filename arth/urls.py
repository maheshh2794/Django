from django.urls import path
from arth import views

urlpatterns = [
    path("add/<int:a>/<int:b>", views.add, name="addition"),
    path("sub/<int:a>/<int:b>", views.sub, name= "subtraction"),
    path("mul/", views.multiply, name="prod"),
    path("div/", views.divide, name="diff"),
    path("mult/",views.multi, name = "product"),
    path('mulresult/',views.multifun, name="multiname")
]