from django import forms

class InternshipForm(forms.Form):
  internship_name = forms.CharField(label="Internship Name", max_length=30)
  company_name = forms.CharField(label="Company Name", max_length=30)
  link = forms.CharField(label="Link", max_length=200)
  description = forms.CharField(label="Description", max_length=200)