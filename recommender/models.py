from django.db import models

# Create your models here.

class CareerInput(models.Model):
    SUBJECT_CHOICES = [
        ('math', 'Mathematics'),
        ('science', 'Science'),
        ('english', 'English'),
        ('art', 'Art'),
        ('history', 'History'),
        ('computer', 'Computer Studies'),
    ]

    INTEREST_CHOICES = [
        ('tech', 'Technology'),
        ('health', 'Healthcare'),
        ('business', 'Business'),
        ('arts', 'Arts'),
        ('education', 'Education'),
    ]

    SKILL_CHOICES = [
        ('problem_solving', 'Problem Solving'),
        ('creativity', 'Creativity'),
        ('communication', 'Communication'),
        ('leadership', 'Leadership'),
        ('teamwork', 'Teamwork'),
    ]

    name = models.CharField(max_length=100)
    selected_subjects = models.JSONField()
    selected_interests = models.JSONField()
    selected_skills = models.JSONField()
    recommended_career = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
