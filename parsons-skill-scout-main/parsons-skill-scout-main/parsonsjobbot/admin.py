from django.contrib import admin
from .models import UploadedFile, Candidate, JobSubmission, UploadedXlsx, XlsxJob, UploadedSOW, SOWPosition, SimilarityScoreMatcher
from django.utils.html import format_html

# Register your models here.


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file']

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['user','name', 'skills', 'years_of_experience', 'education', 'resume']

@admin.register(JobSubmission)
class JobSubmissionAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'position_id', 'position_description', 'skill_level']

@admin.register(UploadedXlsx)
class UploadedXlsxAdmin(admin.ModelAdmin):
    list_display = ['id', 'file']

@admin.register(XlsxJob)
class XlsxJobsAdmin(admin.ModelAdmin):
    list_display = ['tonum', 'posnum', 'open_or_closed','pdnum', 'previous_names', 'project', 'status', 'labor_cat', 'level', 'clin', 'location', 'release_date']
    list_filter = ['tonum', 'open_or_closed', 'level']

@admin.register(UploadedSOW)
class UploadedSOWsAdmin(admin.ModelAdmin):
    list_display = ['id', 'file']

@admin.register(SOWPosition)
class SOWPositionsAdmin(admin.ModelAdmin):
    list_display = ['tonum', 'pos_id', 'posnum', 'posdescnum', 'posdesctitle', 'posdesc_preview', 'level', 'service_cat', 'job_title']
    list_filter = ['tonum', 'level']

@admin.register(SimilarityScoreMatcher)
class SimilarityScoreMatcherAdmin(admin.ModelAdmin):
    list_display = ['candidate_name', 'candidate_info', 'sow_info', 'similarity_score']
    list_filter = ['candidate_name']