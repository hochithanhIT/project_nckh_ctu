from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
# from playground.views import serve_image_and_label
from playground.views import AcneDetectionView

urlpatterns = [
    # path('api/files/<str:filename>/', serve_image_and_label.as_view(), name='image_and_label_file'),
    path('detect/', AcneDetectionView.as_view(), name='detect'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
