from rest_framework import routers
from .api import UserProfessionalViewSet,UserPersonalViewSet,BidsViewSet

router = routers.DefaultRouter()
router.register('api/user',UserProfessionalViewSet,'user')
router.register('api/userp',UserPersonalViewSet,'userp')
router.register('api/bids',BidsViewSet,'bids')


urlpatterns = router.urls
