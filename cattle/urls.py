from django.urls import path
from .views import CattleList, CattleDetail

urlpatterns = [
    path("", CattleList.as_view(), name="cattle_list"),
    path("<int:pk>/", CattleDetail.as_view(), name="cattle_detail")
]