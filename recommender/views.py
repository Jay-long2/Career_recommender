from django.shortcuts import render
from .forms import CareerInputForm
from .models import CareerInput
# Create your views here.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import joblib
from .forms import CareerInputForm

# Load model and encoder
model = joblib.load('career_model.pkl')
target_encoder = joblib.load('career_target_encoder.pkl')

def predict_career(request):
    prediction = None
    graph_url = None

    if request.method == 'POST':
        form = CareerInputForm(request.POST)
        if form.is_valid():
            # Get input from form
            O = form.cleaned_data['O_score']
            C = form.cleaned_data['C_score']
            E = form.cleaned_data['E_score']
            A = form.cleaned_data['A_score']
            N = form.cleaned_data['N_score']
            numerical = form.cleaned_data['Numerical_Aptitude']
            spatial = form.cleaned_data['Spatial_Aptitude']
            perceptual = form.cleaned_data['Perceptual_Aptitude']
            abstract = form.cleaned_data['Abstract_Reasoning']
            verbal = form.cleaned_data['Verbal_Reasoning']

            # Format data for prediction
            input_data = pd.DataFrame([[
                O, C, E, A, N, numerical, spatial,
                perceptual, abstract, verbal
            ]], columns=[
                'O_score', 'C_score', 'E_score', 'A_score', 'N_score',
                'Numerical Aptitude', 'Spatial Aptitude', 'Perceptual Aptitude',
                'Abstract Reasoning', 'Verbal Reasoning'
            ])

            pred = model.predict(input_data)
            career = target_encoder.inverse_transform(pred)[0]
            prediction = f"Recommended Career: {career}"

            # data for the visualization 
            data = {
                'O_score': O,
                'C_score': C,
                'E_score': E,
                'A_score': A,
                'N_score': N,
                'Numerical Aptitude': numerical,
                'Spatial Aptitude': spatial,
                'Perceptual Aptitude': perceptual,
                'Abstract Reasoning': abstract,
                'Verbal Reasoning': verbal
                   }

            # Visualization (bar chart)
            plt.figure(figsize=(10, 5))
            sns.barplot(x=list(data.keys()), y=list(data.values()), palette='Blues_r')
            plt.title(f"Profile for Career Prediction: {career}")
            plt.xticks(rotation=45)
            plt.tight_layout()

            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            image_png = buf.getvalue()
            graph_url = 'data:image/png;base64,' + base64.b64encode(image_png).decode('utf-8')            
        
    else:
        form = CareerInputForm()

    return render(request, 'recommender/predict.html', {
        'form': form,
        'prediction': prediction,
        'graph': graph_url
    })


def home(request):
    return render(request, 'recommender/home.html')

def about(request):
    return render(request, 'recommender/about.html')
