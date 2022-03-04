from django import forms

class InternshipForm(forms.Form):
  internship_name = forms.CharField(label="Internship Name", max_length=30)
  company_name = forms.CharField(label=)