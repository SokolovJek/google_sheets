from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from my_app.views import OrdersModelViewSet


router = DefaultRouter()
router.register('drf_data_table', OrdersModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

]

