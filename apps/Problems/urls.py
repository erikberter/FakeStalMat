from django.urls import path
from . import views

app_name = 'problems'

urlpatterns = [
    path('problem/create/', views.CreateProblem.as_view(), name='problemCreate'),
    path('problem/<int:pk>/', views.DetailProblem.as_view(), name='problemDetail'),
    path('problem/list/', views.ProblemListView.as_view(), name='problemList'),
    path('getPDF/', views.createPDF, name="createPDF"),
]