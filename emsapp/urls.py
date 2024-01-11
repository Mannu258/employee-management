from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('add',views.add_employee,name='add'),
    path('remove/<int:id>',views.remove_employee,name='remove'),
    path('update/<int:id>',views.update,name='update'),
    path('filter',views.filter_employee,name='filter'),

]