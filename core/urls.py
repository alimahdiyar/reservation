from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import (CreateReservationView, ListReservationsView)

schema_view = get_schema_view(
   openapi.Info(
      title="Reservation API",
      default_version='v1',
      contact=openapi.Contact(email="alimahdiyar77@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('reservation/create/', CreateReservationView.as_view()),
    path('reservation/list/', ListReservationsView.as_view()),

    # docs
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]