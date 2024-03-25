from django.urls import path

from . import views

#APP NAME IS THIS NOT JUST jobbot !!!!!!!!!
app_name = 'parsonsjobbot'

urlpatterns = [
    #
    # Url Patterns are expressed on this app as "http://127.0.0.1:8000/jobbot/... where the ... is the url for the paths as seen below"
    #
    # general website stuff
    path('', views.HomeView.as_view(), name='home'),
    path('landing_page/', views.redirect_to_landing_page, name='redirect-to-landing-page'),
    path('resume/', views.ResumeView.as_view(), name='resume-home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('metrics/', views.MetricsView.as_view(), name='metrics'),

    # profile suff
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.EditProfileView.as_view(), name='edit-profile'),

    # candidate stuff
    path('candidates/', views.CandidateView.as_view(), name='candidates'),
    path('candidates/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate-detail'),
    path('candidates/my_candidate', views.MyCandidateProfileView.as_view(), name='my-candidate-profile'),
    path('candidates/<int:pk>/matched', views.CandidateDetailMatchedView.as_view(), name='candidate-detail-matched'),
    
    #job stuff
    path('job_submission/', views.JobSubmissionView.as_view(), name='job-submission'),
    path('job_xlsx_submission/', views.XlsxSubmissionView.as_view(), name='job-xlsx-submission'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),

    #sow stuff
    path('sow_submission/', views.SOWSubmissionView.as_view(), name='sow-submission'),

    #Xlsx and SOW matching stuff
    path('xlsx-sow-open-matcher/', views.XlsxSOWOpenMatcherView.as_view(), name='xlsx-sow-open'),
    path('xlsx-sow-open-matcher/<int:pk>/', views.XlsxSOWOpenDeatilView.as_view(), name='xlsx-sow-open-detail'),
    path('xlsx-sow-open-matcher/<int:pk>/detail', views.XlsxSOWOpenDeatilMatchView.as_view(), name='xlsx-sow-open-detail-match'),
    

    #out of service links for now
    #path('job-rec/<int:pk>/', views.JobDetailView.as_view(), name='job-rec-detail'),
    #path('candidates/<int:pk>/job_list', views.MatchedJobsView.as_view(), name='job-list'),
]