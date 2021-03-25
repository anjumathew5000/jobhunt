
from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name="index"),
    path('reg',views.reg,name="reg"),
    path('regdata',views.regdata,name='regdata'),
    path('regtable',views.regtable,name='regtable'),
    path('deleteobject/<int:dataid>/',views.deleteobject,name='deleteobject')

]
