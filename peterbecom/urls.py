from django import http
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = staticfiles_urlpatterns()

urlpatterns += [
    path("api/v0/", include("peterbecom.api.urls", namespace="api")),
    path("api/v1/", include("peterbecom.publicapi.urls", namespace="publicapi")),
    path("plog/", include("peterbecom.plog.urls")),
    path("minimalcss/", include("peterbecom.minimalcss.urls")),
    path("chiveproxy", lambda x: http.HttpResponseRedirect("/chiveproxy/")),
    path("chiveproxy/", include("peterbecom.chiveproxy.urls")),
    path("oidc/", include("mozilla_django_oidc.urls")),
    path("", include("peterbecom.homepage.urls", namespace="homepage")),
]
