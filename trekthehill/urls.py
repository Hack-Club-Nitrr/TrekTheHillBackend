from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from team import views as team_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'team', team_views.TeamView)

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')), 
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('api/', include(router.urls)),
    path('', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "TREK THE HILL"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Portal"

