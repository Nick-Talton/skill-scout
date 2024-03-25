from django import forms
from django.core.exceptions import ValidationError
import os
from django.contrib.auth.models import User

class ResumeUploadForm(forms.Form):
    """
    If you want to make more fields to put in for the HTML for resume uploading put them here first and then use the variable name
    in the views similarly to the others to make another field.
    """
    resume = forms.FileField(label='Upload Resume', widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}))
    years_of_experience = forms.IntegerField(label='Years of Experience')
    education = forms.CharField(label='Education', max_length=255)
    name = forms.CharField(label='Name', max_length=255)
    is_own_resume = forms.BooleanField(label='Is this your own resume?', required=False)

    def clean_resume(self):
        resume = self.cleaned_data['resume']
        filename = resume.name
        allowed_extensions = ['.pdf', '.doc', '.docx']
        ext = os.path.splitext(filename)[1].lower()


        if ext not in allowed_extensions:
            raise ValidationError("Unsupported file extension. Please upload a PDF, DOC, or DOCX file.")


        return resume
    
class XlsxUploadForm(forms.Form):
    """
    If you want to make more fields to put in for the HTML for resume uploading put them here first and then use the variable name
    in the views similarly to the others to make another field.
    """
    xlsx = forms.FileField(label='Upload Xlsx', widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}))

    def clean_xlsx(self):
        xlsx = self.cleaned_data['xlsx']
        filename = xlsx.name
        allowed_extensions = ['.xlsx']
        ext = os.path.splitext(filename)[1].lower()


        if ext not in allowed_extensions:
            raise ValidationError("Unsupported file extension. Please upload a XLSX file.")


        return xlsx

class SOWUploadForm(forms.Form):
    """
    If you want to make more fields to put in for the HTML for resume uploading put them here first and then use the variable name
    in the views similarly to the others to make another field.
    """
    sow = forms.FileField(label='Upload SOW', widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}))

    def clean_sow(self):
        sow = self.cleaned_data['sow']
        filename = sow.name
        allowed_extensions = ['.pdf', '.docx', '.doc']
        ext = os.path.splitext(filename)[1].lower()


        if ext not in allowed_extensions:
            raise ValidationError("Unsupported file extension. Please upload a PDF or DOCX file.")


        return sow

class UserSelectionForm(forms.Form):
    """
    
    This form is intended to swap a user out with a floating candidate

    NOT IMPLEMENTED AS OF NOW (1/5/2024)
    
    """
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select a user")
