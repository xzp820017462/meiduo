from django.conf.urls import url
from . import views
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^',include('apps.users.urls'))
    url(r'^register/$',views.RegisterView.as_view()),
    #panduan username is_register
    url(r'^usernames/?P<username>([a-zA-z0-9_-]){5,20}/count/$',views.UsermeCountView.as_view()),


]