from django import forms
from .models import CareerInput

class CareerInputForm(forms.ModelForm):
    selected_subjects = forms.MultipleChoiceField(
        choices=CareerInput.SUBJECT_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Subjects"
    )
    selected_interests = forms.MultipleChoiceField(
        choices=CareerInput.INTEREST_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Interests"
    )
    selected_skills = forms.MultipleChoiceField(
        choices=CareerInput.SKILL_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Skills"
    )

    class Meta:
        model = CareerInput
        fields = ['name', 'selected_subjects', 'selected_interests', 'selected_skills']
        
class CareerInputForm(forms.Form):
    O_score = forms.FloatField(label="Openness")
    C_score = forms.FloatField(label="Conscientiousness")
    E_score = forms.FloatField(label="Extraversion")
    A_score = forms.FloatField(label="Agreeableness")
    N_score = forms.FloatField(label="Neuroticism")
    Numerical_Aptitude = forms.FloatField()
    Spatial_Aptitude = forms.FloatField()
    Perceptual_Aptitude = forms.FloatField()
    Abstract_Reasoning = forms.FloatField()
    Verbal_Reasoning = forms.FloatField()
