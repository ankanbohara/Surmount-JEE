from django.conf.urls import url
from . import views
from .feeds import LatestEntriesFeed
app_name = 'form'
urlpatterns = [url(r'^$',views.index,name='index'),
               url(r'^aboutus/$',views.aboutus,name='aboutus'),
               url(r'^quizmultiple/$',views.quizmorethanone,name='quizmorethanone'),
               url(r'^quizsingle/$',views.quizsingle,name='quizsingle'),
               url(r'^syllabus/$',views.syllabus,name='syllabus'),
               url(r'^feedbackform/$',views.feedback,name="feedback"),
               url(r'^newregistration/$',views.registration,name = 'registration'),
               url(r'^newlogin/$',views.loginview,name='loginview'),
               url(r'^success/$',views.success,name='success'),
               url(r'^contact/$',views.contact,name='contact'),
               url(r'^contactsuccess/$',views.enquiry,name='enquiry'),
               url(r'^blogform/$',views.blog,name='blog'),
               url(r'^logout/$',views.log_out,name="log_out"),
               #url(r'^ifuser$',views.userlogin,name='userlogin')
               #url(r'^result_page/$', views.result_page, name='result_page'),
               url(r'^certificate/$', views.certificate_page, name='certificate_page'),
               url(r'^answerpage/$', views.answerpage, name='answerpage'),
               url(r'^answerpagemulti/$', views.answerpagemulti, name='answerpagemulti'),
               #url(r'^result_pagemulti/$', views.result_pagemulti, name='result_pagemulti'),
               url(r'^viewblogs/$',views.viewblogs,name='viewblogs'),
               url(r'^notifications/$',views.notification,name='notification'),
               url(r'^performance/$',views.performance,name='performance'),
               url(r'^latest/feed/$', LatestEntriesFeed(),name='feed'),
               ]