

import os
import pickle
import numpy as np
from django.shortcuts import render
from django.conf import settings
from .forms import PredictorForm
from .ml_model import model



def heart_predict(request):
    result = None
    if request.method == 'POST':
        form = PredictorForm(request.POST)
        if form.is_valid():
           
            data = [
                form.cleaned_data['age'],
                form.cleaned_data['gender'],
                form.cleaned_data['blood_pressure'],
                form.cleaned_data['cholesterol'],
                form.cleaned_data['pulse'],
            ]
            arr = np.array(data, dtype=float).reshape(1, -1)
            pred = model.predict(arr)[0]
            result = 'możesz mieć chorobe serca' if pred == 1 else 'Prawdopodobnie nie masz choroby serca'
    else:
        form = PredictorForm()

    return render(request, 'predictor/heart_form.html', {
        'form': form,
        'result': result
    })
