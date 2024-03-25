from django.db import models

from django.contrib.auth.models import Group, User

# Create your models here.

#test model idk if we need it
# class Employee(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     years_of_experience = models.IntegerField()
#     job_title = models.CharField(max_length=100)
#     skills = models.TextField()


#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


# from django.db import models

#dont forget to migrate!!!

class Candidate(models.Model):
    """
    This model creates a candidate class that maintains a one to one relationship with the user and holds onto information such as: 
    User, name, skills, yoe, education, and resume
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    skills = models.TextField()
    years_of_experience = models.IntegerField()
    education = models.CharField(max_length=255)
    resume = models.ForeignKey('UploadedFile', on_delete=models.CASCADE, null=True)
    # add more fields as per your requirements


    def __str__(self):
        return self.name

class UploadedFile(models.Model):
    """
    This class (not sure If we technically need it for now but I think its good to keep on file in case) maintains all files uploaded to the database
    """
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.file.name

class Skill(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class JobSubmission(models.Model):
    position_id = models.CharField(max_length=50)
    position_description = models.IntegerField()
    skill_level = models.IntegerField()
    job_title = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill)


    def __str__(self):
        return f"{self.job_title} ({self.position_id})"

class UploadedXlsx(models.Model):
    """
    This class maintains all xlsx files uploaded to the database
    """
    file = models.FileField(upload_to='SOWs/')

    def __str__(self):
        return self.file.name

class XlsxJob(models.Model):
    tonum = models.CharField(max_length=100) 
    posnum = models.CharField(max_length=100)
    pdnum = models.CharField(max_length=100) 
    previous_names = models.CharField(max_length=100) 
    project = models.CharField(max_length=100) 
    status = models.CharField(max_length=100)
    labor_cat = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    clin = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    open_or_closed = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"This is Position can be found on TONum: {self.tonum} (Position: {self.posnum}) and this position is {self.open_or_closed}."

class UploadedSOW(models.Model):
    """
    This class maintains all SOW files uploaded to the database
    """

    file = models.FileField(upload_to='SOWs/')

    def __str__(self):
        return self.file.name

class SOWPosition(models.Model):
    tonum = models.CharField(max_length=100)
    pos_id = models.CharField(max_length=100)
    posnum = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posdescnum = models.CharField(max_length=100)
    posdesctitle = models.CharField(max_length=100)
    posdesc = models.TextField(default='Position Description Goes Here')
    level = models.CharField(max_length=100)
    service_cat = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    #xlsx_job = models.ForeignKey(XlsxJob, on_delete=models.CASCADE, related_name='sow_positions', null=True)

    def __str__(self):
        return f"This is SOW Position {self.pos_id} found on Task Order {self.tonum}"
    
    @property
    def posdesc_preview(self):
        preview_length = 100  # Adjust the desired length
        if len(self.posdesc) > preview_length:
            return self.posdesc[:preview_length] + "..."
        return self.posdesc

    class Meta:
        verbose_name_plural = 'SOW Positions'

class SimilarityScoreMatcher(models.Model):
    candidate_name = models.CharField(max_length=255)
    candidate_info = models.TextField()
    #sow_pos = models.CharField(max_length=255)
    sow_info = models.TextField()
    similarity_score = models.FloatField()

    def __str__(self):
        return f"Candidate {self.candidate_name} has a similarity score of {self.similarity_score} for the position"
    
    @property
    def candidate_info_preview(self):
        preview_length = 100  # Adjust the desired length
        if len(self.candidate_info) > preview_length:
            return self.candidate_info[:preview_length] + "..."
        return self.candidate_info

    @property
    def sow_info_preview(self):
        preview_length = 100  # Adjust the desired length
        if len(self.sow_info) > preview_length:
            return self.sow_info[:preview_length] + "..."
        return self.sow_info