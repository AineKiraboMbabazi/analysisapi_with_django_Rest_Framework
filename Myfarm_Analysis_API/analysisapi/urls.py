from django.urls import path
from .apiviews import AssociationList, AssociationDetail, GovernmentDetail,GovernmentList


urlpatterns = [
    path("associations/", AssociationList.as_view(), name="get_associations_list"),
    path("associations/<int:pk>", AssociationDetail.as_view(), name="get_association_details"),
    path("governments/", GovernmentList.as_view(), name="get_governments_list"),
    path("governments/<int:pk>", GovernmentDetail.as_view(), name="get_governments_details"),

]