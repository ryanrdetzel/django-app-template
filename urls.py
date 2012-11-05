from django.conf import settings
from django.conf.urls.defaults import include, patterns

from {{ app_name }}.views import hello


urlpatterns = patterns('',
    (r'^hello/$', hello),
)
