from rest_framework.routers import DefaultRouter
import men_data.api.views as views

router_posts = DefaultRouter()
router_posts.register(prefix='men_info',basename='men_info',viewset=views.InfoApiViewSet)
router_posts.register(prefix='first_question',basename='first_question',viewset=views.FirstApiViewSet)
