from django import forms

class PredictorForm(forms.Form):
    AGE_CHOICES = [(i, i) for i in range(1, 121)]
    GENDER_CHOICES = [
        (0, 'Kobieta'),
        (1, 'Mężczyzna'),
    ]
    age = forms.IntegerField(label='Wiek', min_value=1, max_value=120)
    gender = forms.ChoiceField(label='Płeć', choices=GENDER_CHOICES)
    blood_pressure = forms.IntegerField(label='Ciśnienie krwi (mmHg)', min_value=30, max_value=300)
    cholesterol = forms.IntegerField(label='Cholesterol (mg/dL)', min_value=35, max_value=1000)
    pulse = forms.IntegerField(label='Puls (uderzeń/min)', min_value=30, max_value=300)

