from django.shortcuts import render
import numpy as np
from .forms import PredictorForm
from .ml_model import scaler, knn

def heart_predict(request):
    result = None
    if request.method == 'POST':
        form = PredictorForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = int(form.cleaned_data['gender'])
            bp = form.cleaned_data['blood_pressure']
            chol = form.cleaned_data['cholesterol']
            pulse = form.cleaned_data['pulse']

            X_new = np.array([[age, gender, bp, chol, pulse]])
            X_scaled = scaler.transform(X_new)

           
            label = knn.predict(X_scaled)[0]
          
            if label == 1:
                result = "Prawdopodobnie Masz chorobę serca"
            else:
                result = "Prawdopodobnie Nie masz choroby serca"
    else:
        form = PredictorForm()

    return render(request, 'predictor/heart_form.html', {
        'form': form,
        'result': result,
    })

