from rest_framework.routers import DefaultRouter
import men_data.api.views as views

router_posts = DefaultRouter()
router_posts.register(prefix='men_info',basename='men_info',viewset=views.InfoApiViewSet)
router_posts.register(prefix='first_question',basename='first_question',viewset=views.FirstApiViewSet)
router_posts.register(prefix='second_question',basename='second_question',viewset=views.SecondApiViewSet)
router_posts.register(prefix='third_question',basename='third_question',viewset=views.ThirdApiViewSet)
router_posts.register(prefix='fourth_question',basename='fourth_question',viewset=views.FourthApiViewSet)
router_posts.register(prefix='fifth_question',basename='fifth_question',viewset=views.FifthApiViewSet)
