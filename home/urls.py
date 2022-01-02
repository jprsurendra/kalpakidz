from django.urls import path
from home import views

urlpatterns = [
    # path(r'^', TemplateView.as_view(template_name='homeapp/index.html')),
    path('', views.index, name='index'),
    # path(r'^$', TemplateView.as_view(template_name='homeapp/index.html')),
    # url(r'^', TemplateView.as_view(template_name='homeapp/index.html')),
    # url(r'^admin/', admin.site.urls),

]
