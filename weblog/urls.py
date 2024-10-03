from django.urls import path
from weblog.views import homepage,aboutpage,weblogDetailview,weblogcreateView,weblogupdateview,weblogdeleteview

urlpatterns = [
    path('',homepage.as_view(), name='home'),
    path('about',aboutpage.as_view(), name='about'),
    path('details/<int:pk>/',weblogDetailview.as_view(),name='details'),
    path('new_post',weblogcreateView.as_view(),name='new_post'),
    path('update/<int:pk>/',weblogupdateview.as_view(),name='update'),
    path('delete/<int:pk>/',weblogdeleteview.as_view(),name='delete')
]
