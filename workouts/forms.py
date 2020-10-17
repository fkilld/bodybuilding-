from django import forms
from django.forms import ModelForm
from .models import Workout, Member


class DateInput(forms.DateInput):
    input_type = 'date'


class WorkoutForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = Member.objects.filter(user_id=user)

    class Meta:
        model = Workout
        fields = '__all__'
        widgets = {'date_of_working': DateInput()}


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['profile_pic']