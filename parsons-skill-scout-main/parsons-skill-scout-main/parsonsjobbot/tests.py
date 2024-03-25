from django.test import TestCase, Client
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Candidate, Skill, JobSubmission, XlsxJob, SOWPosition, UploadedSOW, UploadedXlsx
from .views import calculate_score, redirect_to_landing_page, reorganize_dict, extract_positions_from_excel, parse_tables_and_position_descs_word, compute_similarity_percentage, get_candidate_for_position, get_open_positions_for_candidate

from pyresparser import ResumeParser
from docx import Document
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import pandas as pd
import re
nlp = spacy.load('en_core_web_sm')

class CandidateModelTestCase(TestCase):
    def setUp(self):
        self.candidate = Candidate.objects.create(
            name="John Doe",
            skills="Python, Django, SQL",
            years_of_experience=3,
            education="Bachelor's Degree",
        )

    def test_candidate_creation(self):
        self.assertEqual(self.candidate.name, "John Doe")
        self.assertEqual(self.candidate.skills, "Python, Django, SQL")
        self.assertEqual(self.candidate.years_of_experience, 3)
        self.assertEqual(self.candidate.education, "Bachelor's Degree")

class ResumeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

class CandidateViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Assuming you have created a user and assigned them to a group like 'Employee'
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user.groups.add(Group.objects.get(name='Employee'))
        self.client.login(username='testuser', password='testpassword')

class CandidateModelTestCase(TestCase):
    def test_candidate_creation(self):
        candidate = Candidate.objects.create(
            name="John Doe",
            skills="Python, Django, SQL",
            years_of_experience=3,
            education="Bachelor's Degree",
        )
        self.assertEqual(candidate.name, "John Doe")
        self.assertEqual(candidate.skills, "Python, Django, SQL")
        self.assertEqual(candidate.years_of_experience, 3)
        self.assertEqual(candidate.education, "Bachelor's Degree")

class SkillModelTestCase(TestCase):
    def test_skill_creation(self):
        skill = Skill.objects.create(name="Python")
        self.assertEqual(skill.name, "Python")

class JobSubmissionModelTestCase(TestCase):
    def test_xlsx_job_creation(self):
        xlsx_job = XlsxJob.objects.create(
            tonum="TONum123",
            posnum="PosNum123",
            pdnum="PDNum123",
            previous_names="PreviousNames",
            project="ProjectABC",
            status="Open",
            labor_cat="Category1",
            level="Level2",
            clin="CLIN123",
            location="LocationXYZ",
            release_date="2023-07-19",
            open_or_closed="open",
        )
        self.assertEqual(xlsx_job.tonum, "TONum123")
        self.assertEqual(xlsx_job.posnum, "PosNum123")
        self.assertEqual(xlsx_job.pdnum, "PDNum123")
        self.assertEqual(xlsx_job.previous_names, "PreviousNames")
        self.assertEqual(xlsx_job.project, "ProjectABC")
        self.assertEqual(xlsx_job.status, "Open")
        self.assertEqual(xlsx_job.labor_cat, "Category1")
        self.assertEqual(xlsx_job.level, "Level2")
        self.assertEqual(xlsx_job.clin, "CLIN123")
        self.assertEqual(xlsx_job.location, "LocationXYZ")
        self.assertEqual(xlsx_job.release_date, "2023-07-19")
        self.assertEqual(xlsx_job.open_or_closed, "open")

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a user for testing authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.group = Group.objects.create(name='Employee')
        self.user.groups.add(self.group)

        # Create some test data for Candidate and JobSubmission models
        self.candidate = Candidate.objects.create(
            user=self.user,
            name='Test Candidate',
            skills='Skill1, Skill2',
            years_of_experience=5,
            education='Bachelor of Science',
        )
        self.job_submission = JobSubmission.objects.create(
            position_id='123',
            position_description=1,
            skill_level=2,
            job_title='Test Job',
        )

    def test_home_view(self):
        response = self.client.get(reverse('parsonsjobbot:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Skill Scout")

    def test_resume_view(self):
        # Simulate authentication
        self.client.login(username='testuser', password='testpassword')
        
        response = self.client.get(reverse('parsonsjobbot:resume-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Resume Submission")

    def test_metrics_view(self):
        response = self.client.get(reverse('parsonsjobbot:metrics'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Metrics")

    def test_candidate_detail_view_authenticated(self):
        # Simulate authentication
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('parsonsjobbot:candidate-detail', args=[self.candidate.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Candidate")
        self.assertContains(response, "Matched Jobs")

    def test_about_view(self):
        response = self.client.get(reverse('parsonsjobbot:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About")

    def test_profile_view_unauthenticated(self):
        response = self.client.get(reverse('parsonsjobbot:profile'))
        self.assertEqual(response.status_code, 200)  # Allows access to unauthenticated users

    def test_edit_profile_view_unauthenticated(self):
        response = self.client.get(reverse('parsonsjobbot:edit-profile'))
        self.assertEqual(response.status_code, 302)  # Redirects to login page

    def test_post_edit_profile_view(self):
        # Simulate authentication
        self.client.login(username='testuser', password='testpassword')

        # Prepare form data for POST request
        form_data = {
            'name': 'Updated User',
            'groups': [self.group.pk],
        }
        response = self.client.post(reverse('parsonsjobbot:edit-profile'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirects to profile page

        # Check if user details are updated
        updated_user = User.objects.get(username='testuser')
        self.assertEqual(updated_user.first_name, 'Updated')
        self.assertEqual(updated_user.last_name, 'User')
        self.assertEqual(list(updated_user.groups.all()), [self.group])

class AdditionalViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a user for testing authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.group_employee = Group.objects.create(name='Employee')
        self.group_external = Group.objects.create(name='External')
        self.user.groups.add(self.group_employee)
    
    # Create some test objects for the views
        self.xlsx_job = XlsxJob.objects.create(
            tonum='TONUM1',
            posnum='POSNUM1',
            open_or_closed='open',
        )

        self.sow_position = SOWPosition.objects.create(
            tonum='TONUM1',
            pos_id='POSID1',
            posnum='POSNUM1',
            location='Location1',
            posdescnum='PosDescNum1',
            posdesctitle='PosDescTitle1',
            posdesc='Position Description 1',
            level='Level1',
            service_cat='ServiceCat1',
            job_title='JobTitle1',
        )

        self.candidate = Candidate.objects.create(
            user=self.user,
            name='Test Candidate',
            skills='Skill1, Skill2',
            years_of_experience=2,
            education='Education1',
        )



