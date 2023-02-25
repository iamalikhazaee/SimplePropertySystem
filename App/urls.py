from rest_framework.routers import DefaultRouter
from django.urls import path, include
from App import views


router = DefaultRouter()

router.register(r'Profile', views.ProfileViewSet)
router.register(r'Role', views.RoleViewSet)
router.register(r'Sell_Contract', views.SellContractViewSet)
router.register(r'Rent_Contract', views.RentContractViewSet)
router.register(r'Sell_Property', views.SellPropertyViewSet)
router.register(r'Rent_Property', views.RentPropertyViewSet)
router.register(r'Customer', views.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
