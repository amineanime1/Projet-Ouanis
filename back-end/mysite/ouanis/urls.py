from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from .views import ExpediteurViewSet, VoyageurViewSet, AnnonceViewSet, DemandeAnnonceViewSet, DemandeColisViewSet, DemandeCourierViewSet, DemandeDeCompteVoyageurViewSet

router = DefaultRouter()
router.register(r'expediteurs', ExpediteurViewSet)
router.register(r'voyageurs', VoyageurViewSet)
router.register(r'recherche', AnnonceViewSet)
router.register(r'demandes-annonces', DemandeAnnonceViewSet)
router.register(r'demandes-colis', DemandeColisViewSet)
router.register(r'deman des-couriers', DemandeCourierViewSet)
router.register(r'demandes-compte-voyageurs', DemandeDeCompteVoyageurViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 