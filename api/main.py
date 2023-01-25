from fastapi import FastAPI
from .app.models import PredictionResponse, PredictionRequest
from .app.views import get_predictions

# la documentacion para correr nuestra api estará en el root
app = FastAPI(docs_url='/')

@app.post('/v1/prediction')
def make_model_prediction(request: PredictionRequest):
    return PredictionResponse(worldwide_gross = get_predictions(request))
