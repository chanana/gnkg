from django import forms


class dnaStringSubmission(forms.Form):
    job_name = forms.CharField(label="Job Title")
    dna_string = forms.CharField(
        label="DNA Sequence", widget=forms.Textarea, max_length=1000
    )
