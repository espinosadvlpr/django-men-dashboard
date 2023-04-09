from rest_framework.routers import DefaultRouter
from men_data.api.views import InfoApiViewSet

router_posts = DefaultRouter()
router_posts.register(prefix='men_info',basename='men_info',viewset=InfoApiViewSet)
