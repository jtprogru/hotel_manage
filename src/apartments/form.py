from django.db.models import Q
from django import forms

from .models import Passport, Client


class PassportCreationForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = ["serial", "number", "police_department", "police_department_id",
                  "date_issue", "sex", "birth_date", "birth_place", "registration"]

    def date_of_birth(self):
        return self.birth_date

