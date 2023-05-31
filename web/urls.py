from django.urls import path
from .views import main, about, projects, collections, contactus, detailprojects, \
    detailcollections, contactdetail, signin, signup, logoutView, adminPanel
urlpatterns = [
    path('', main.as_view(), name="main"),
    path('adminpanel/', adminPanel, name="adminpanel"),
    path('about/', about.as_view(), name="about"),
    path('projects/', projects.as_view(), name="projects"),
    path('collections/', collections.as_view(), name="collections"),
    path('contact/', contactus.as_view(), name="contact"),
    path('contactdetail/<int:pk>', contactdetail.as_view(), name="contactdetail"),
    path('detail-projects/<int:pk>', detailprojects.as_view(), name="detail-projects"),
    path('detail-collections/<int:pk>', detailcollections.as_view(), name="detail-collections"),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logoutView, name='logout'),
]
